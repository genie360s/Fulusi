import scrapy

class MkomboziSpider(scrapy.Spider):

    name = "mkombozi"

    start_urls = ['http://mkombozibank.co.tz/',
                  ]
    
    def parse(self, response):
        exchange_rate_marquee = response.css('marquee')
        exchange_rate_marquee_li = exchange_rate_marquee.css('li')
        currencies = exchange_rate_marquee_li.css('span.currency-init::text').getall()
        print(currencies)
        buying_and_selling_rates = exchange_rate_marquee_li.css('span.currency-val::text').getall()
        print(buying_and_selling_rates)
        rates = []
        buying_rates = []
        selling_rates = []
        for buying_and_selling_rate in buying_and_selling_rates:
            rates.append(float(buying_and_selling_rate.strip().replace(',','')))
            print(rates)
        for rate in rates:
            if rates.index(rate) % 2 == 0:
                buying_rates.append(rate)
                print(buying_rates)
            else:
                selling_rates.append(rate)
                print(selling_rates)

        for currency, buying_rate, selling_rate in zip(currencies, buying_rates, selling_rates):
            yield {
                'currency': currency.strip() if currency else None,
                'buying': float(buying_rate if buying_rate else None),
                'selling':float(selling_rate if selling_rate else None),
            }

        