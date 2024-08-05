import scrapy
from finscrap.items import NmbItem
class NmbSpider(scrapy.Spider):
    name = 'nmb'
    start_urls = ['https://www.nmbbank.co.tz/', 
                  ]
    
    def parse(self, response):
        exchange_rate_marquee = response.css('marquee')
        print(exchange_rate_marquee.get())
        exchange_rate_marquee_rows = exchange_rate_marquee.css('li')
        exchange_rate_datas = []
        for exchange_rate_marquee_row in exchange_rate_marquee_rows:
            exchange_rate_data = exchange_rate_marquee_row.css('span::text').getall()
            del exchange_rate_data[1]
            del exchange_rate_data[2:4]
            exchange_rate_datas.append(exchange_rate_data)
            print(exchange_rate_datas)
        
        for exchange_rate_data in exchange_rate_datas:
            yield NmbItem (
                currency = exchange_rate_data[0].strip().replace(':','') if exchange_rate_data[0] else None,
                buying_price = float(exchange_rate_data[1].strip().replace(',', '') if exchange_rate_data[1] else None),
                selling_price = float(exchange_rate_data[2].strip().replace(',', '') if exchange_rate_data[2] else None),
            )
        
