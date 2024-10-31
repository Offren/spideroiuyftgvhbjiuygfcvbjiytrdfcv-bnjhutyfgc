import scrapy
import csv
import os
from pathlib import Path
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
            data_dir = Path(__file__).parent.parent / 'data'
            urls_file = data_dir / 'URLs.csv'
            
            with open(urls_file, 'r', encoding='utf-8') as f:
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
            data_dir = Path(__file__).parent.parent / 'data'
            xpath_file = data_dir / 'xpath.csv'
            
            with open(xpath_file, 'r', encoding='utf-8') as f:
                for line in f:
                    xpath = line.strip()
                    if xpath:
                        xpaths.append(xpath)
            self.logger.info(f"Loaded {len(xpaths)} XPath patterns")
        except Exception as e:
            self.logger.error(f"Error loading XPaths: {e}")
        return xpaths

    def parse(self, response):
        # Try each XPath pattern for profile URLs
        for xpath in self.xpaths:
            profile_urls = response.xpath(xpath).getall()
            if profile_urls:
                for url in profile_urls:
                    # Make sure URL is absolute
                    full_url = response.urljoin(url)
                    item = ProfileItem()
                    item['url'] = full_url
                    item['source_url'] = response.url
                    yield item
