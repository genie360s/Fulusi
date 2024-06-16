import scrapy
from finscrap.items import BoiItem
class BoiSpider(scrapy.Spider):
    name = "boi"
    start_urls = ['https://boitanzania.co.tz/',]

    def parse(self, response):
        # Selecting the tbody element directly
        table = response.css('tbody')
        rows = table.css('tr')

        # Defining the split_into_groups function
        def split_into_groups(lst, group_size):
            return [lst[i:i+group_size] for i in range(0, len(lst), group_size)]

        # Iterating over each row in the table
        for row in rows:
            currency_datas = row.css('td div::text').getall()
            currency_datas = [data.strip() for data in currency_datas]

            # Splitting currency_datas into groups of 3
            groups = split_into_groups(currency_datas, 3)

            # Do something with the groups (for example, print them)
            for group in groups:
               # Check if group has at least 3 elements before accessing group[2]
                if len(group) >= 3:
                    yield BoiItem (
                        currency = group[0] if group[0] else None,
                        buying_price = float(group[1]) if group[1] else None,
                        selling_price = float(group[2]) if group[2] else None,
                    )
                else:
                    yield BoiItem (
                        currency = float(group[0]) if group[0] else None,
                        buying_price = float(group[1]) if group[1] else None,
                        selling_price = None,
                    )
