import json

class GoodreadsScraperPipeline:
    def __init__(self):
        self.file = open('profiles.json', 'w')
        self.profiles = set()

    def process_item(self, item, spider):
        if item['url'] not in self.profiles:
            self.profiles.add(item['url'])
            line = json.dumps(dict(item)) + "\n"
            self.file.write(line)
        return item
        
    def close_spider(self, spider):
        self.file.close()