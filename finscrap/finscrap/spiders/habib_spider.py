import scrapy

class HabibSpider(scrapy.Spider):
    name = "habib"

    start_urls = ['https://habibafricanbank.co.tz/',
    ]

    def parse(self, response):
        exchange_rate_div_block = response.css('div.mtphr-dnt-tick-contents')
        exchange_rate_div_block_inner_divs = exchange_rate_div_block.css('div.mtphr-dnt-tick.mtphr-dnt-default-tick.mtphr-dnt-clearfix')  
        print(exchange_rate_div_block_inner_divs.get())
        exchange_rate_datas = []
        for exchange_rate_inner_div in exchange_rate_div_block_inner_divs:
            exchange_rate_data = exchange_rate_inner_div.css('span::text').getall()
            del exchange_rate_data[1]
            del exchange_rate_data[2]
            exchange_rate_datas.append(exchange_rate_data)
            print(exchange_rate_datas)

        for exchange_rate_data in exchange_rate_datas:
            yield {
                'currency': exchange_rate_data[0].strip() if exchange_rate_data[0] else None,
                'buying': float(exchange_rate_data[1].strip().replace(',','') if exchange_rate_data[1] else None),
                'selling': float(exchange_rate_data[2].strip().replace(',','')  if exchange_rate_data[2] else None),
            }