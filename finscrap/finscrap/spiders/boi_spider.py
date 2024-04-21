import scrapy

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
                print(group)
                yield {
                    'currency_data' : group,
                }
