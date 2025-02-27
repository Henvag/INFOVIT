import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def get_first_paragraph(url):
    #Fetch and return the first meaningful paragraph from the given Wikipedia article.
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise an error for bad responses
        soup = BeautifulSoup(response.text, 'html.parser')

        # Select paragraphs within the main content area
        for p in soup.select('.mw-parser-output > p'):
            text = p.get_text(strip=True)
            if text and len(text) > 50:  # Ensure the paragraph has meaningful content
                return text
        return "No valid paragraph found."

    except requests.RequestException as e:
        return f"Error fetching {url}: {e}"


def scrape_see_also_links():
    """Extract 'See also' links from the Web Scraping Wikipedia page and print their first paragraphs."""
    start_url = "https://en.wikipedia.org/wiki/Web_scraping"

    try:
        response = requests.get(start_url, timeout=5)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Locate the 'See also' section
        see_also = soup.find('div', class_='div-col')
        if not see_also:
            print("No 'See also' section found.")
            return

        # Extract and process each link
        for link in see_also.find_all('a', href=True):
            article_url = urljoin(start_url, link['href'])
            print(f"\nArticle: {link.text}")
            print(f"URL: {article_url}")
            print("First paragraph:")
            print(get_first_paragraph(article_url))

    except requests.RequestException as e:
        print(f"Error fetching {start_url}: {e}")


# Run the scraper
scrape_see_also_links()