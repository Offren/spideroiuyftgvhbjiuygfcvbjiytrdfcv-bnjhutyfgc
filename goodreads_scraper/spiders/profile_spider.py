import scrapy
import csv
from goodreads_scraper.items import ProfileItem

class ProfileSpider(scrapy.Spider):
    name = 'profiles'
    allowed_domains = ['goodreads.com']
    
    def __init__(self, *args, **kwargs):
        super(ProfileSpider, self).__init__(*args, **kwargs)
        self.start_urls = self.load_urls()
        self.xpaths = self.load_xpaths()
        
    def load_urls(self):
        urls = []
        with open('URLs.csv', 'r') as f:
            for line in f:
                url = line.strip()
                if url:
                    urls.append(url)
        return urls
        
    def load_xpaths(self):
        xpaths = []
        with open('xpath.csv', 'r') as f:
            for line in f:
                xpath = line.strip()
                if xpath:
                    xpaths.append(xpath)
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