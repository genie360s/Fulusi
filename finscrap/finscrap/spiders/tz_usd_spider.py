import scrapy 

class TzUsdSpider(scrapy.Spider):
    name = "tz_usd"

    start_urls = ['https://www.bot.go.tz/FinancialMarket/ifem',
                  ]
    
    def parse(self, response):
        table = response.css('table')
        table_body = table.css('tbody')
        table_rows = table_body.css('tr')
        # tz_forex_usd_datas = table_rows.css('td::text').getall()
        tz_forex_usd_datas = []
        for row in table_rows:
            tz_forex_usd_data = row.css('td::text').getall()
            tz_forex_usd_datas.append(tz_forex_usd_data)
        
        for tz_forex_usd_data in tz_forex_usd_datas:

            yield {
            
            'date': tz_forex_usd_data[1].strip() if tz_forex_usd_data[1] else None,
            'amount': tz_forex_usd_data[2].strip().replace(",", "") if tz_forex_usd_data[2] else None,
            'high': tz_forex_usd_data[3].strip().replace(",", "") if tz_forex_usd_data[3] else None,
            'low': tz_forex_usd_data[4].strip().replace(",", "") if tz_forex_usd_data[4] else None,
            'average': tz_forex_usd_data[5].strip().replace(",", "") if tz_forex_usd_data[5] else None,
            }