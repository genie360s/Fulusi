import scrapy
from finscrap.items import TcbItem
class TcbSpider(scrapy.Spider):
    name = "tcb"

    start_urls = ['https://www.tcbbank.co.tz/home/en',]

    def parse(self, response):
        exchange_rate_marquee = response.css('marquee')
        exchange_rate_ul = exchange_rate_marquee.css('ul')
        exchange_rate_li = exchange_rate_ul.css('li')
        exchange_rate_b = exchange_rate_ul.css('b::text').getall()
        exchange_rate_blocks = exchange_rate_li.css('::text').getall()
        

        exchange_rate_currencies = []
        for currency in exchange_rate_b:
            exchange_rate_currencies.append(currency.strip().replace(" ","").replace(":",""))
            print(exchange_rate_currencies)

        
        selling_prices = []
        buying_prices = []

        for price in exchange_rate_blocks:
            price_split_colon = price.split(":")
            buying_selling_prices = price_split_colon[0].split("-")

            if len(buying_selling_prices) == 2:
                buying_prices.append(buying_selling_prices[0].strip().replace("Buy","").replace(",","").replace(" ","").strip())
                print(buying_prices)
                selling_prices.append(buying_selling_prices[1].strip().replace("Sell","").replace(",","").replace(" ","").strip())
                print(selling_prices)

                for curreny_name, buying_price, selling_price in zip(exchange_rate_currencies, buying_prices, selling_prices):
                    yield TcbItem (
                        currency = curreny_name.strip() if curreny_name else None,
                        buying_price = float(buying_price) if buying_price else None,
                        selling_price = float(selling_price) if selling_price else None
                    )