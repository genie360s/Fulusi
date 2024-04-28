import scrapy

class BotSpider(scrapy.Spider):
    name = "bot"
    start_urls = ['https://www.bot.go.tz/',
                  ]
    
    def parse(self, response):
        exchange_rate_block = response.css('div.card-body.card-show-table')
        exchange_rate_time = exchange_rate_block.css('div[style="padding-left:10px; font-weight:bold"]::text').get()
        exchange_rate_time = exchange_rate_time.strip().replace("Transaction Date:","") if exchange_rate_time else None
        exchange_rate_table = exchange_rate_block.css('table.table.table-sm.table-bordered.table-hover.p-0')
        exchange_rate_table_body = exchange_rate_table.css('tbody')
        exchange_rate_table_rows = exchange_rate_table_body.css('tr')
        exchange_rate_datas = []
        for row in exchange_rate_table_rows:
            exchange_rate_data = row.css('td::text').getall()
            exchange_rate_datas.append(exchange_rate_data)
            print(exchange_rate_datas)
        
        for data in exchange_rate_datas:
            yield {
                'currency': data[0].strip() if data else None,
                'buying': float(data[1].strip()) if data else None,
                'selling': float(data[2].strip()) if data else None,
            }