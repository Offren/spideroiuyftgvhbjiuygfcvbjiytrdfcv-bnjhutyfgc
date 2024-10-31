import scrapy
import csv
import os
import pkgutil
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
            # Load URLs from package data
            urls_data = pkgutil.get_data('goodreads_scraper', 'data/URLs.csv')
            if urls_data:
                for line in urls_data.decode('utf-8').splitlines():
                    url = line.strip()
                    if url:
                        urls.append(url)
            else:
                self.logger.error("URLs.csv not found in package data")
        except Exception as e:
            self.logger.error(f"Error loading URLs: {e}")
        return urls
        
    def load_xpaths(self):
        xpaths = []
        try:
            # Load XPaths from package data
            xpath_data = pkgutil.get_data('goodreads_scraper', 'data/xpath.csv')
            if xpath_data:
                for line in xpath_data.decode('utf-8').splitlines():
                    xpath = line.strip()
                    if xpath:
                        xpaths.append(xpath)
            else:
                self.logger.error("xpath.csv not found in package data")
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
