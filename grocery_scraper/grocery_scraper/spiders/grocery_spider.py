
import scrapy
from bs4 import BeautifulSoup
import json

class GrocerySpider(scrapy.Spider):
    name = "grocery"
    start_urls = [
        'http://example.com/grocery-deals',
    ]

    def parse(self, response):
        soup = BeautifulSoup(response.body, 'html.parser')
        deals = []
        for item in soup.select('.deal-item'):
            deal = {
                'name': item.select_one('.deal-name').text,
                'price': item.select_one('.deal-price').text,
                'store': response.url,
            }
            deals.append(deal)
        with open('deals.json', 'w') as f:
            json.dump(deals, f)
                    