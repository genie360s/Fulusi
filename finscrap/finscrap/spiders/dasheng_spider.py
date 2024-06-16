import scrapy
from finscrap.items import DashengItem
class DangshengSpider(scrapy.Spider):
    name = "dasheng"
    start_urls =['https://chinadashengbank.co.tz/',
                 ]
    
    def parse(self, response):
        sell_data = response.css('strong::text').getall()
        strong = response.css('strong')
        buy_data = strong.css('span::text').getall()
        note_types = []
        large_notes = sell_data[0]
        small_notes = sell_data[2]
        note_types.append(large_notes)
        note_types.append(small_notes)
        sell_large_note = sell_data[1].replace("Sell", "").strip()
        sell_small_note = sell_data[3].replace("Sell", "").strip()
        selling_prices = []
        selling_prices.append(sell_large_note)
        selling_prices.append(sell_small_note)

        buying_prices = []
        for data in buy_data:
            data = data.replace("Buy", "").strip()
            buying_prices.append(data)

        for note_type, selling_price, buying_price in zip(note_types, selling_prices, buying_prices):
            yield DashengItem (
                currency = note_type,
                buying_price = float(buying_price),
                selling_price = float(selling_price), 
            )