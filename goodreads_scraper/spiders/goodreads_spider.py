import scrapy
import os
from goodreads_scraper.items import ProfileItem

class GoodreadsSpider(scrapy.Spider):
    name = 'goodreads'
    allowed_domains = ['goodreads.com']
    
    def __init__(self, *args, **kwargs):
        super(GoodreadsSpider, self).__init__(*args, **kwargs)
        # Get the project root directory
        project_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        
        # Load URLs and XPaths from project root
        self.urls_file = os.path.join(project_dir, 'URLs.csv')
        self.xpath_file = os.path.join(project_dir, 'xpath.csv')
        
        self.start_urls = self.load_urls()
        self.xpaths = self.load_xpaths()
        
    def load_urls(self):
        urls = []
        try:
            with open(self.urls_file, 'r') as f:
                for line in f:
                    url = line.strip()
                    if url:
                        urls.append(url)
            return urls
        except FileNotFoundError:
            self.logger.error(f"URLs file not found at {self.urls_file}")
            return []
        
    def load_xpaths(self):
        xpaths = []
        try:
            with open(self.xpath_file, 'r') as f:
                for line in f:
                    xpath = line.strip()
                    if xpath:
                        xpaths.append(xpath)
            return xpaths
        except FileNotFoundError:
            self.logger.error(f"XPaths file not found at {self.xpath_file}")
            return []

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
