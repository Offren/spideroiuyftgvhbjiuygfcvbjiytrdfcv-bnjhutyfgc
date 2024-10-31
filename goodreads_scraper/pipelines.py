import json
from scrapy.exceptions import DropItem

class GoodreadsScraperPipeline:
    def __init__(self):
        self.profiles = set()

    def process_item(self, item, spider):
        if item['url'] not in self.profiles:
            self.profiles.add(item['url'])
            return item
        raise DropItem(f"Duplicate profile found: {item['url']}")

    def close_spider(self, spider):
        spider.logger.info(f"Total unique profiles found: {len(self.profiles)}")
