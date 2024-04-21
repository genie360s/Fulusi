import scrapy
from scrapy.selector import Selector

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
                yield {
                    'fund_name': fund_name.strip() if fund_name else None,
                    'fund_date': fund_date.strip() if fund_date else None,
                    'fund_description': fund_description.strip() if fund_description else None,
                    'data': {
                        "Net Asset Value (Tsh)" : data_values[0].strip() if data_values else None,
                        "Outstanding Number of Units (Tsh)" : data_values[1].strip() if len(data_values) > 1 else None,
                        "Net Asset Value Per Unit (Tsh)" : data_values[2].strip() if len(data_values) > 2 else None,
                        "Sale Price Per Unit (Tsh)" : data_values[3].strip() if len(data_values) > 3 else None,
                        "Purchase Price Per Unit (Tsh)" : data_values[4].strip() if len(data_values) > 4 else None,
                    }
                }

    # def parse(self, response):
    #     fund_descriptions = response.css('div.our-product').getall()
    #     for fund_description in fund_descriptions:
    #         fund_description_selector = Selector(text=fund_description)
    #         fund_description = fund_description_selector.css('p.description::text').getall()
    #         yield {
    #             'fund_description': fund_description
    #         }