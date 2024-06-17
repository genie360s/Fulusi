import scrapy
from scrapy.selector import Selector
from finscrap.items import UttAmisItem
class UttAmis(scrapy.Spider):
    name = "utt_amis"

    start_urls = [
        'https://uttamis.co.tz/',
    ]

    def parse(self, response):
        # Extract the text from the h3 element with class "mtab"
        fund_names = response.css('h3.mtab::text').getall()
        fund_date = response.xpath('//th[@colspan="5"]/text()').get()
        fund_data_tables = response.css('div.tdataTable table').getall()        
        fund_descriptions = response.css('p.description::text').getall()

        # Extracting data from the tables
        for fund_name, fund_description, fund_data_table in zip(fund_names, fund_descriptions, fund_data_tables):
            # Creating a selector objects
            table_selector = Selector(text=fund_data_table)
            # Extracting table data
            fund_data_table_rows = table_selector.css('tbody tr')
            for row in fund_data_table_rows[1:]:
                data_values = row.css('td::text').getall()
                # Yielding results
                
                yield UttAmisItem (
                    fund_name = fund_name.strip() if fund_name else None,
                    fund_date = fund_date.strip() if fund_date else None,
                    data = {
                        "net_asset_value_tzs" : float(data_values[0].strip().replace(",","").replace(" ", "")) if data_values[0] else None,
                        "outstanding_number_of_units_tzs" : float(data_values[1].strip().replace(",","").replace(" ", "")) if data_values[1] else None,
                        "net_asset_value_per_unit_tzs" : float(data_values[2].strip().replace(",","").replace(" ", "")) if data_values[2] else None,
                        "sale_price_per_unit_tzs" : float(data_values[3].strip().replace(",","").replace(" ", "")) if data_values[3] else None,
                        "purchase_price_per_unit_tzs" : float(data_values[4].strip().replace(",","").replace(" ", "")) if data_values[4] else None,
                    }
                )