import scrapy
from scrapy import Request
from wikispider.items import Article

class Article1Spider(scrapy.Spider):
    name = "article1"

    def start_requests(self):
        urls = [
            'https://en.wikipedia.org/wiki/Python_(programming_language)',
            'https://en.wikipedia.org/wiki/Java_(Functional_programming)',
            'https://en.wikipedia.org/wiki/Monty_Python',
        ]
        return [Request(url=url, callback=self.parse) for url in urls]

    def parse(self, response):
        article = Article()
        article['url'] = response.url
        article['title'] = response.xpath('//h1/span/text()').extract_first()
        lastUpdated = response.xpath("//*[@id='footer-info-lastmod']/text()").extract_first()
        article['lastUpdated'] = lastUpdated.replace('This page was last edited on ', '')
        return article