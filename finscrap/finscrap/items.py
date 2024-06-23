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
    buying_price_tt_od = scrapy.Field()
    selling_price_tt_od = scrapy.Field()
    selling_fc_notes = scrapy.Field()
    buying_fc_notes_less_50_euro_usd = scrapy.Field()
    buying_fc_notes_more_50_euro_usd = scrapy.Field()

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

class FaidaItem(scrapy.Item):
    date = scrapy.Field()
    net_asset_value_tzs = scrapy.Field()
    outstanding_number_of_units = scrapy.Field()
    nav_per_unit_tzs = scrapy.Field()
    sales_price_per_unit_tzs = scrapy.Field()
    repurchase_price_per_unit_tzs = scrapy.Field()

class UttAmisItem(scrapy.Item):
    fund_name = scrapy.Field()
    fund_date = scrapy.Field()
    fund_description = scrapy.Field()
    data = scrapy.Field()
    data['net_asset_value_tzs'] = scrapy.Field()
    data['outstanding_number_of_units_tzs'] = scrapy.Field()
    data['net_asset_value_per_unit_tzs'] = scrapy.Field()
    data['sale_price_per_unit_tzs'] = scrapy.Field()
    data['purchase_price_per_unit_tzs'] = scrapy.Field()

class CorporateBondsItem(scrapy.Item):
    issuer = scrapy.Field()
    issued_date = scrapy.Field()
    coupon_rate = scrapy.Field()
    issued_amount = scrapy.Field()
    term_years = scrapy.Field()
    maturity_date = scrapy.Field()

class GovernmentBondsItem(scrapy.Item):
    issuer = scrapy.Field()
    issued_date = scrapy.Field()
    maturity_date = scrapy.Field()
    coupon_rate = scrapy.Field()
    issued_amount = scrapy.Field()
    term_years = scrapy.Field()
    