import scrapy
from finscrap.items import TcbItem
class TcbSpider(scrapy.Spider):
    name = "tcb"

    start_urls = ['https://www.tcbbank.co.tz/home/en',]

    def parse(self, response):
        # @todo: update the extraction with respect to the new website layout
        exchange_rate_div_block = response.css('div.newssectionPad.yellow_bg')
        print(exchange_rate_div_block.get())
        exchange_rate_date = exchange_rate_div_block.css('p::text').get()
        exchange_rate_date = exchange_rate_date.strip().replace("Updated On :","") if exchange_rate_date else None
        exchange_rate_table = exchange_rate_div_block.css('table')
        exchange_rate_table_rows = exchange_rate_table.css('tr')
        currency_names_td  = exchange_rate_table_rows.css('td')
        currency_names_p = currency_names_td.css('p')
        currency_names = currency_names_p.css('b::text').getall()
        print(currency_names)
        
        print(exchange_rate_table_rows.get())

        exchange_rate_datas = []

        for row in exchange_rate_table_rows:
            exchange_rate_td = row.css('td')
            exchange_rate_data = exchange_rate_td.css('p::text').getall()
            exchange_rate_datas.append(exchange_rate_data)

        for curreny_name, data in zip(currency_names, exchange_rate_datas[1:]):
            yield TcbItem (
                currency = curreny_name.strip() if curreny_name else None,
                buying_price = float(data[0].strip().replace(',','') if data[0] else None),
                selling_price = float(data[1].strip().replace(',', '') if data[1] else None),
            )