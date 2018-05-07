from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose


def convert_price(value):
    return float(value.strip(' $ '))


class OfferLoader(ItemLoader):
    default_output_processor = TakeFirst()
    price_in = MapCompose(convert_price)
    old_price_in = MapCompose(convert_price)
