import scrapy
from finscrap.items import AzaniaItem
class AzaniaSpider(scrapy.Spider):
    name = "azania"
    start_urls = ['https://azaniabank.co.tz/'
                  ,]
    
    def parse(self, response):
        exchange_rate_datas = []
        exchange_rate_data_div_blocks = response.css('div.symbol_line')
        
        print(exchange_rate_data_div_blocks.get())

        for exchange_rate_data_div_block in exchange_rate_data_div_blocks:
            exchange_rate_data_div_block_spans = exchange_rate_data_div_block.css('span::text').getall()
            exchange_rate_datas.append(exchange_rate_data_div_block_spans)
            print(exchange_rate_datas)  

        for exchange_rate_data in exchange_rate_datas:
            yield AzaniaItem(
                currency = exchange_rate_data[0].strip().replace(':',''),
                buying_price = float(exchange_rate_data[1].strip().replace(',', '')),
                selling_price = float(exchange_rate_data[2].strip().replace(',', '')),
            )