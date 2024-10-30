from scrapy import Item, Field

class ProfileItem(Item):
    url = Field()
    source_url = Field()