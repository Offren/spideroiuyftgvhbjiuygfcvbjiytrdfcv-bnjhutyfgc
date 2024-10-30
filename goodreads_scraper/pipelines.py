import logging

class GoodreadsScraperPipeline:
    def __init__(self):
        self.urls_seen = set()
        self.logger = logging.getLogger(__name__)

    def process_item(self, item, spider):
        if 'url' in item:
            if item['url'] in self.urls_seen:
                self.logger.debug(f'Duplicate URL found: {item["url"]}')
                return None
            self.urls_seen.add(item['url'])
            self.logger.info(f'New URL processed: {item["url"]}')
        return item
