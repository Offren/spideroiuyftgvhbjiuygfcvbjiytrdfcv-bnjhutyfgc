import scrapy
from goodreads_scraper.items import ProfileItem
from goodreads_scraper.data import URLS, XPATHS

class GoodreadsSpider(scrapy.Spider):
    name = 'goodreads'
    allowed_domains = ['goodreads.com']
    custom_settings = {
        'CONCURRENT_REQUESTS': 1,
        'DOWNLOAD_DELAY': 3,
        'COOKIES_ENABLED': False
    }
    
    def __init__(self, *args, **kwargs):
        super(GoodreadsSpider, self).__init__(*args, **kwargs)
        self.start_urls = URLS
        self.xpaths = XPATHS
        self.logger.info(f"Loaded {len(self.start_urls)} URLs")
        self.logger.info(f"Loaded {len(self.xpaths)} XPath patterns")

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url,
                callback=self.parse,
                errback=self.errback_httpbin,
                dont_filter=True
            )

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

    def errback_httpbin(self, failure):
        self.logger.error(f"Request failed: {failure.request.url}")
