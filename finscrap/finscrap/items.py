# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FinscrapItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class AmanaItem(scrapy.Item):
    currency = scrapy.Field()
    buying_price = scrapy.Field()
    selling_price = scrapy.Field()

class AzaniaItem(scrapy.Item):
    currency = scrapy.Field()
    buying_price = scrapy.Field()
    selling_price = scrapy.Field()

class BarodaItem(scrapy.Item):
    currency = scrapy.Field()
    buying_price = scrapy.Field()
    selling_price = scrapy.Field()

class BoiItem(scrapy.Item):
    currency = scrapy.Field()
    buying_price = scrapy.Field()
    selling_price = scrapy.Field()

class BotItem(scrapy.Item):
    currency = scrapy.Field()
    buying_price = scrapy.Field()
    selling_price = scrapy.Field()

class DashengItem(scrapy.Item):
    currency = scrapy.Field()
    buying_price = scrapy.Field()
    selling_price = scrapy.Field()

class DcbItem(scrapy.Item):
    currency = scrapy.Field()
    buying_price = scrapy.Field()
    selling_price = scrapy.Field()

class HabibItem(scrapy.Item):
    currency = scrapy.Field()
    buying_price = scrapy.Field()
    selling_price = scrapy.Field()

class IcbItem(scrapy.Item):
    currency = scrapy.Field()
    buying_price = scrapy.Field()
    selling_price = scrapy.Field()

class MkomboziItem(scrapy.Item):
    currency = scrapy.Field()
    buying_price = scrapy.Field()
    selling_price = scrapy.Field()

class NmbItem(scrapy.Item):
    currency = scrapy.Field()
    buying_price = scrapy.Field()
    selling_price = scrapy.Field()

class TcbItem(scrapy.Item):
    currency = scrapy.Field()
    buying_price = scrapy.Field()
    selling_price = scrapy.Field()
