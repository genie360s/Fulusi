import scrapy

class IcbSpider(scrapy.Spider):
    name = 'icb'

    start_urls = ['https://icbank.co.tz/',
                  ]
    
    def parse(self, response):
        exchange_rate_div_block = response.css('div.cmsmasters_wrap_table')
       
        exchange_rate_table = exchange_rate_div_block.css('table.cmsmasters_table.foreign-exchange-rates-box')
        exchange_rate_table_body = exchange_rate_table.css('tbody')
        exchange_rate_table_rows = exchange_rate_table_body.css('tr')
        exchange_rate_datas = []
        for exchange_rate_table_row in exchange_rate_table_rows:
            exchange_rate_data = exchange_rate_table_row.css('td::text').getall()
            exchange_rate_datas.append(exchange_rate_data)
            

        for exchange_rate_data in exchange_rate_datas:
            yield {
                'currency': exchange_rate_data[0].strip() if exchange_rate_data[0] else None,
                'Selling (TT/OD)': float(exchange_rate_data[1].strip() if exchange_rate_data[1] else None),
                'Buying(TT/OD)': float(exchange_rate_data[2].strip() if exchange_rate_data[2] else None),
                'Selling FC Notes': float(exchange_rate_data[3].strip() if exchange_rate_data[3] else None),
                'Buying FC Notes(<50$/50Euro)': float(exchange_rate_data[4].strip() if exchange_rate_data[4] else None),
                'Buying FC Notes(>=50$/50Euro)': float(exchange_rate_data[5].strip() if exchange_rate_data[5] else None),
            }