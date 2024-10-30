import scrapy
from goodreads_scraper.items import BookItem

class GoodreadsSpider(scrapy.Spider):
    name = 'goodreads'
    allowed_domains = ['goodreads.com']
    start_urls = ['https://www.goodreads.com/search?q=social+justice+books']

    def parse(self, response):
        # List of XPath patterns to try for each book URL
        url_xpaths = [
            '//div[contains(@class, "article")]//section[2]/span[1]/div/a/@href',
            '//div[contains(@class, "bookTitle")]/@href',
            '//a[contains(@class, "bookTitle")]/@href'
        ]
        
        # Try each XPath pattern
        for xpath in url_xpaths:
            urls = response.xpath(xpath).getall()
            if urls:
                for url in urls:
                    # Make sure URL is absolute
                    full_url = response.urljoin(url)
                    item = BookItem()
                    item['url'] = full_url
                    yield item

        # Follow pagination links
        next_page = response.xpath('//a[contains(@class, "next_page")]/@href').get()
        if next_page:
            yield response.follow(next_page, self.parse)