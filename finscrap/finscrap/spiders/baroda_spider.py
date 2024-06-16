import scrapy
from finscrap.items import BarodaItem
class BarodaSpider(scrapy.Spider):
    name = "baroda"
    start_urls = ['https://www.bankofbaroda.co.tz/indicative-forex-exchange',
    ]

    def parse(self, response):
        exchange_rate_table = response.css('table.responsiveTable.tableData')
        print(exchange_rate_table)
        exchange_rate_table_rows = exchange_rate_table.css('tr')
        exchange_rate_datas = []
        for exchange_rate_table_row in exchange_rate_table_rows[1:]:
            exchange_rate_data  = exchange_rate_table_row.css('td::text').getall()
            del exchange_rate_data[0]
            
            exchange_rate_datas.append(exchange_rate_data)
            print(exchange_rate_datas)

        for exchange_rate_data in exchange_rate_datas:
            yield BarodaItem (
                currency = exchange_rate_data[0].strip() if exchange_rate_data[0].strip() != '' else 'USD',
                buying_price = float(exchange_rate_data[1].strip().replace(',','') if exchange_rate_data[1] else None),
                selling_price = float(exchange_rate_data[2].strip().replace(',','') if exchange_rate_data[2]  else None),
            )