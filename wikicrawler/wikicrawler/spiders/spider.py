import extruct
import time
import logging
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

def process_links(links):
    for link in links:
        yield link
        
class WikiCrawler(CrawlSpider):
    name = 'wiki'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Georgia_Tech']
    count = 0

    rules = (
        Rule(
            LinkExtractor(),
            process_links=process_links,
            callback='parse_item',
            follow=True
        ),
    )

    def parse_item(self, response):
        stats = self.crawler.stats.get_stats()
        self.count += 1
        return {
            'url': response.url,
            'time': time.time(),
            'num_scheduled': stats["scheduler/enqueued"],
            'num_scraped': self.count,
            'metadata': extruct.extract(
                response.text,
                response.url
            ),
        }

    custom_settings = {
        "BOT_NAME": "Wiki Crawler",
    }
