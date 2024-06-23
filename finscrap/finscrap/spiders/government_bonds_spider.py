import scrapy
from finscrap.items import GovernmentBondsItem
class CorporateBondsSpider(scrapy.Spider):
    name = "government_bonds"

    start_urls = ['https://dse.co.tz/government/bond',]

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
            # variables are issuer , issued date , coupon rate, issued amount (float), term (int), maturity date

            yield GovernmentBondsItem(
                issuer = data[0].strip() if data[0] else None,
                issued_date = data[1].strip() if data[1] else None,
                maturity_date = data[2].strip() if data[2] else None,
                coupon_rate = safe_float_conversion(data[3]) if data[2] else None,
                issued_amount = float(data[4].replace(",","").replace("USD","").strip()) if data else None,
                term_years = int(data[5].replace("Years", "").strip()) if data[5] else None,
            )
