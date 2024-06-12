import scrapy

class GroceryScraperItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    store = scrapy.Field()