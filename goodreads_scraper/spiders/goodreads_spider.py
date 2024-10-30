import scrapy
from goodreads_scraper.items import BookItem
import logging

class GoodreadsSpider(scrapy.Spider):
    name = 'goodreads'
    allowed_domains = ['goodreads.com']
    start_urls = ['https://www.goodreads.com/search?q=social+justice+books']
    
    custom_settings = {
        'CONCURRENT_REQUESTS_PER_DOMAIN': 1,
        'DOWNLOAD_DELAY': 3
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url=url,
                callback=self.parse,
                dont_filter=True,
                meta={'dont_redirect': False, 'handle_httpstatus_list': [301, 302]}
            )

    def parse(self, response):
        self.logger.info(f'Parsing page: {response.url}')
        
        # List of XPath patterns to try for each book URL
        url_xpaths = [
            '//div[contains(@class, "article")]//section[2]/span[1]/div/a/@href',
            '//div[contains(@class, "bookTitle")]/@href',
            '//a[contains(@class, "bookTitle")]/@href',
            '//tr[@itemtype="http://schema.org/Book"]//a[@class="bookTitle"]/@href',
            '//div[contains(@class, "left") and contains(@class, "container")]//a[contains(@class, "bookTitle")]/@href'
        ]
        
        urls_found = False
        # Try each XPath pattern
        for xpath in url_xpaths:
            urls = response.xpath(xpath).getall()
            if urls:
                urls_found = True
                self.logger.info(f'Found {len(urls)} URLs using pattern: {xpath}')
                for url in urls:
                    # Make sure URL is absolute
                    full_url = response.urljoin(url)
                    item = BookItem()
                    item['url'] = full_url
                    yield item
        
        if not urls_found:
            self.logger.warning(f'No URLs found on page: {response.url}')
            self.logger.debug(f'Page content: {response.text[:1000]}')

        # Follow pagination links
        next_page = response.xpath('//a[contains(@class, "next_page")]/@href').get()
        if next_page:
            self.logger.info(f'Following next page: {next_page}')
            yield response.follow(
                next_page,
                callback=self.parse,
                meta={'dont_redirect': False, 'handle_httpstatus_list': [301, 302]}
            )
