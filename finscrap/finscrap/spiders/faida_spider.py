import scrapy
from finscrap.items import FaidaItem
class FaidaSpider(scrapy.Spider):
    name = "faida"

    start_urls = ['https://www.whi.go.tz/NavData/NavEnglish.php',]

    def parse(self, response):
        table = response.css('table')
        table_body = table.css('tbody')
        table_rows = table_body.css('tr:nth-last-child(2)')
        current_fund_data = table_rows.css('td::text').getall()
        
        yield FaidaItem (
            date = current_fund_data[0].strip() if current_fund_data[0] else None,
            net_asset_value = float(current_fund_data[1].strip().replace(",", "") if current_fund_data[1] else None),
            outstanding_number_of_units = float(current_fund_data[2].strip().replace(",", "") if current_fund_data[2] else None),
            nav_per_unit = float(current_fund_data[3].strip().replace(",", "") if current_fund_data[3] else None),
            sales_price_per_unit = float(current_fund_data[4].strip().replace(",", "") if current_fund_data[4] else None),
            repurchase_price_per_unit = float(current_fund_data[5].strip().replace(",", "") if current_fund_data[5] else None),
        )
        