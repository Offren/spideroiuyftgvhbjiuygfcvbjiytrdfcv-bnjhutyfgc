from scrapy import Item, Field

class BookItem(Item):
    url = Field()
    title = Field()
    author = Field()
    rating = Field()
    description = Field()
