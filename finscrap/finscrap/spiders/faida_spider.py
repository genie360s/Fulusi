import scrapy

class FaidaSpider(scrapy.Spider):
    name = "faida"

    start_urls = ['https://www.whi.go.tz/NavData/NavEnglish.php',]

    def parse(self, response):
        table = response.css('table')
        table_body = table.css('tbody')
        table_rows = table_body.css('tr:nth-last-child(2)')
        current_fund_data = table_rows.css('td::text').getall()
        
        yield {
            'date': current_fund_data[0].strip() if current_fund_data[0] else None,
            'Net Asset Value (Tzs)': current_fund_data[1].strip().replace(",", "") if current_fund_data[1] else None,
            'Outstanding Number of Units': current_fund_data[2].strip().replace(",", "") if current_fund_data[2] else None,
            'Nav Per Unit (Tzs)': current_fund_data[3].strip().replace(",", "") if current_fund_data[3] else None,
            'Sales Price Per Unit (Tzs)': current_fund_data[4].strip().replace(",", "") if current_fund_data[4] else None,
            'Repurchase Price Per Unit (Tzs)': current_fund_data[5].strip().replace(",", "") if current_fund_data[5] else None,
        }
        