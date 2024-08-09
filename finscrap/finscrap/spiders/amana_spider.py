import scrapy
from finscrap.items import AmanaItem
class AmanaSpider(scrapy.Spider):
    name = "amana"

    start_urls = ['https://www.amanabank.co.tz/',
                  ]
    
    def parse(self, response):
        forex_div = response.css('div.js-conveyor-example')
        print(forex_div)
        forex_ul = forex_div.css('ul')
        forex_li = forex_ul.css('li')
        currency_names = forex_li.css('strong::text').getall()
        buying_and_selling_prices = forex_li.css('span::text').getall()
        buying_prices = []
        selling_prices = []
        print(currency_names)
        print(buying_and_selling_prices)
        
        for prices in buying_and_selling_prices:
            prices = prices.split('-')
            buying_price = float(prices[0].strip().replace("Buy", ""))
            selling_price = float(prices[1].strip().replace("Sell", ""))
            buying_prices.append(buying_price)
            selling_prices.append(selling_price)

        for currency_name, buying_price, selling_price in zip(currency_names, buying_prices, selling_prices):
            yield AmanaItem (
                currency = currency_name.replace(':','').strip(),
                buying_price = buying_price,
                selling_price = selling_price
            )
          