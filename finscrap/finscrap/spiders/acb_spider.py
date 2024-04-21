import scrapy

class AcbSpider(scrapy.Spider):
    name = "acb"

    start_urls = [
        'https://www.acbbank.co.tz/',
    ]

    def parse(self, response):
        exchange_rate_div_block = response.css('div.znColumnElement-innerContent')
        print(exchange_rate_div_block.get())
        