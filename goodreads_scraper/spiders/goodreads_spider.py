import scrapy
import csv
import os
from goodreads_scraper.items import ProfileItem

class GoodreadsSpider(scrapy.Spider):
    name = 'goodreads'
    allowed_domains = ['goodreads.com']
    
    def __init__(self, *args, **kwargs):
        super(GoodreadsSpider, self).__init__(*args, **kwargs)
        self.start_urls = self.load_urls()
        self.xpaths = self.load_xpaths()
        
    def load_urls(self):
        urls = []
        try:
            data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'URLs.csv')
            with open(data_path, 'r', encoding='utf-8') as f:
                for line in f:
                    url = line.strip().strip(',')
                    if url:
                        urls.append(url)
            self.logger.info(f"Loaded {len(urls)} URLs")
        except Exception as e:
            self.logger.error(f"Error loading URLs: {e}")
        return urls
        
    def load_xpaths(self):
        xpaths = []
        try:
            data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'xpath.csv')
            with open(data_path, 'r', encoding='utf-8') as f:
                for line in f:
                    xpath = line.strip()
                    if xpath:
                        xpaths.append(xpath)
            self.logger.info(f"Loaded {len(xpaths)} XPath patterns")
        except Exception as e:
            self.logger.error(f"Error loading XPaths: {e}")
        return xpaths

    def parse(self, response):
        for xpath in self.xpaths:
            profile_urls = response.xpath(xpath).getall()
            if profile_urls:
                for url in profile_urls:
                    full_url = response.urljoin(url)
                    item = ProfileItem()
                    item['url'] = full_url
                    item['source_url'] = response.url
                    yield item
