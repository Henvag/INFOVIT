import scrapy
import re
import logging
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


# Defined the item class directly in this file due to issue with importing items
class VergeReview(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    author_name = scrapy.Field()
    author_profile = scrapy.Field()


class VergeReviewsSpider(CrawlSpider):
    name = 'verge_reviews'
    allowed_domains = ['theverge.com']
    start_urls = ['https://www.theverge.com/reviews']

    # Define URL patterns with more relaxed matching
    pattern1 = r'theverge\.com/\d+/[^/]+'
    pattern2 = r'theverge\.com/[a-z-]+/\d+/[^/]+'

    rules = (
        # Rule to follow links matching our patterns
        Rule(LinkExtractor(
            allow=[pattern1, pattern2],
            deny=['/authors/', '/about/', '/contact/', '/advertise/', '/rss/']
        ), callback='parse_review', follow=True),

        # Rule to follow any links within the site
        Rule(LinkExtractor(
            allow_domains=['theverge.com'],
            deny=['/authors/', '/about/', '/contact/', '/advertise/', '/rss/']
        ), follow=True),
    )

    custom_settings = {
        'LOG_LEVEL': 'INFO',
        'DOWNLOAD_DELAY': 0.2,
        'CLOSESPIDER_TIMEOUT': 120,  # 2 minutes
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'verge_reviews.csv',
        'ROBOTSTXT_OBEY': True,
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    }

    def parse_review(self, response):
        """Parse a potential review page"""
        logging.info(f"Parsing potential review: {response.url}")

        # Debug: Print the entire page HTML to a file for inspection
        page_content = response.body.decode('utf-8')
        with open('last_page.html', 'w', encoding='utf-8') as f:
            f.write(page_content)

        # ------------------------
        # Extract Title - with detailed debugging
        # ------------------------
        logging.info("Attempting to find title...")

        # Try direct h1 extraction with multiple approaches
        title = None
        direct_title = response.css('h1::text').get()
        if direct_title and direct_title.strip():
            title = direct_title.strip()
            logging.info(f"Found title with 'h1::text': {title}")
        else:
            # Try nested title extraction
            nested_title = response.css('h1 *::text').get()
            if nested_title and nested_title.strip():
                title = nested_title.strip()
                logging.info(f"Found title with 'h1 *::text': {title}")
            else:
                # Try XPath approach
                xpath_title = response.xpath('//h1//text()').get()
                if xpath_title and xpath_title.strip():
                    title = xpath_title.strip()
                    logging.info(f"Found title with XPath '//h1//text()': {title}")
                else:
                    # Try getting all text nodes within h1 and joining them
                    all_h1_text = response.xpath('//h1//text()').getall()
                    if all_h1_text:
                        title = ' '.join([t.strip() for t in all_h1_text if t.strip()])
                        logging.info(f"Found title by joining all h1 text: {title}")
                    else:
                        # Try specific classes used by The Verge
                        class_title = response.css('.c-page-title::text, .duet--article--headline::text').get()
                        if class_title and class_title.strip():
                            title = class_title.strip()
                            logging.info(f"Found title with class selectors: {title}")

        if not title:
            logging.warning("Could not find title using any method")
            h1_html = response.css('h1').get() or "No h1 element found"
            logging.info(f"H1 HTML structure: {h1_html}")

        # ------------------------
        # Extract Author - with detailed debugging
        # ------------------------
        logging.info("Attempting to find author...")

        author_name = None

        # Try standard author selectors
        standard_author = response.css('a[href*="/authors/"] span::text, a[href*="/author/"] span::text').get()
        if standard_author and standard_author.strip():
            author_name = standard_author.strip()
            logging.info(f"Found author with standard selector: {author_name}")
        else:
            # Try The Verge specific classes
            verge_author = response.css('.duet--article--byline-author-name::text, .c-byline__author-name::text').get()
            if verge_author and verge_author.strip():
                author_name = verge_author.strip()
                logging.info(f"Found author with Verge-specific class: {author_name}")
            else:
                # Try generic byline components
                byline_author = response.css('[data-component="Byline"] a::text, .byline__author-name::text').get()
                if byline_author and byline_author.strip():
                    author_name = byline_author.strip()
                    logging.info(f"Found author with generic byline: {author_name}")
                else:
                    # Last resort: Try to get any text near "By" or within byline sections
                    by_text = response.xpath('//p[contains(text(), "By ")]/text()').get()
                    if by_text and "By " in by_text:
                        author_name = by_text.split("By ")[1].strip()
                        logging.info(f"Found author with 'By' text: {author_name}")
                    else:
                        # Try for meta tags
                        meta_author = response.css('meta[name="author"]::attr(content)').get()
                        if meta_author:
                            author_name = meta_author
                            logging.info(f"Found author in meta tag: {author_name}")

        if not author_name:
            logging.warning("Could not find author using any method")
            byline_html = response.css('[data-component="Byline"], .c-byline, .byline').get() or "No byline found"
            logging.info(f"Byline HTML structure: {byline_html}")

        # ------------------------
        # Extract Author Profile - with less strict requirements
        # ------------------------
        author_profile = (response.css('a[href*="/authors/"]::attr(href), a[href*="/author/"]::attr(href)').get() or
                          response.css('[data-component="Byline"] a::attr(href)').get() or
                          response.css('.c-byline a::attr(href)').get())

        if author_profile:
            logging.info(f"Found author profile: {author_profile}")

        # ------------------------
        # Check if we have enough information to create an item
        # ------------------------

        # IMPORTANT CHANGE: We'll create items even if we're missing the author profile
        # As long as we have a title and author name, we'll create an item
        if title and author_name:
            # Create and return the item
            item = VergeReview()
            item['url'] = response.url
            item['title'] = title
            item['author_name'] = author_name

            # Make sure author profile is a full URL if we have it
            if author_profile:
                if not author_profile.startswith('http'):
                    author_profile = 'https://www.theverge.com' + author_profile
                item['author_profile'] = author_profile
            else:
                # If no profile URL found, we'll just leave it blank
                item['author_profile'] = ''

            logging.info(f"SUCCESS! Created complete item for: {response.url}")
            return item
        else:
            missing_fields = []
            if not title:
                missing_fields.append("title")
            if not author_name:
                missing_fields.append("author name")

            logging.warning(f"Skipping page - missing: {', '.join(missing_fields)}: {response.url}")
            return None