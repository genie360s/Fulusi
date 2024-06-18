import scrapy
from finscrap.items import DashengItem
class DangshengSpider(scrapy.Spider):
    name = "dasheng"
    start_urls =['https://chinadashengbank.co.tz/',
                 ]
    def parse(self, response):
        div_exchange_rate_block = response.css('div.scrolling-text-container')
        span_exchange_rate = div_exchange_rate_block.css('span.exchange-rate')
        span_forex_data = span_exchange_rate.css('span::text').getall()
        print(span_forex_data)
        note_types = ['USD Small Notes', 'USD Large Notes']
        prices = []
        buying_prices = []
        selling_prices = []

        for price in span_forex_data:
            price_split = price.split("-")
            price = price_split[-1].strip().replace(",", "").replace(" ", "")
            if price != '':
                prices.append(price)
                
        for price in prices:
            if prices.index(price) % 2 != 0:
                buying_prices.append(price)
                print(buying_prices)
            else:
                selling_prices.append(price)
                print(selling_prices)
            

        for note_type, selling_price, buying_price in zip(note_types, selling_prices, buying_prices):
            yield DashengItem (
                currency = note_type,
                buying_price = float(buying_price),
                selling_price = float(selling_price), 
            )