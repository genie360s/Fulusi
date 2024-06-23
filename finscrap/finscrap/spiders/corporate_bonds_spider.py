import scrapy
from finscrap.items import CorporateBondsItem
class CorporateBondsSpider(scrapy.Spider):
    name = "corporate_bonds"

    start_urls = ['https://dse.co.tz/corporate/bond',]

    def parse(self, response):
        bond_table = response.css('table.common_table.tableScroll')
        

        bond_table_body = bond_table.css('tbody')
        bond_table_rows = bond_table_body.css('tr')

        bond_datas = []
        for row in bond_table_rows:
            bond_data = row.css('td::text').getall()
            bond_datas.append(bond_data)
            

        def safe_float_conversion(value):
            try:
                return float(value.replace("%", "").strip())
            except ValueError:
                return None

        for data in bond_datas:
            
            #nmb has issues price in USD 
            
            yield CorporateBondsItem(
                issuer = data[0].strip() if data else None,
                issued_date = data[1].strip() if data else None,
                coupon_rate = safe_float_conversion(data[2]) if data[2] else None,
                issued_amount = float(data[3].replace(",","").replace("USD","").strip()) if data else None,
                term_years = int(data[4].replace("Years", "").strip()) if data[4] else None,
                maturity_date = data[5].strip() if data else None,
            )