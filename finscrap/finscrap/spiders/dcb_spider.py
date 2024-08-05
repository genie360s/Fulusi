import scrapy
from finscrap.items import DcbItem
class DcbSpider(scrapy.Spider):
    name = "dcb"
    start_urls = ['https://www.dcb.co.tz/']

    def parse(self, response):
        currency_exchange_rates = response.css('div.currency-rate')
        currency_names = currency_exchange_rates.css('div.name::text').getall()
        selling_buying_rates = currency_exchange_rates.css('div.rate::text').getall()
        
        for rates in selling_buying_rates:
            rates = rates.split('/')
            selling_rate = int(rates[0].strip().replace(",", ""))
            buying_rate = int(rates[1].strip().replace(",", ""))
            yield DcbItem (
                currency = currency_names.pop(0).strip().replace(":","") if currency_names else None,
                buying_price = float(buying_rate),
                selling_price = float(selling_rate),
            )