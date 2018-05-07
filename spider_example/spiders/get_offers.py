# -*- coding: utf-8 -*-
import scrapy

from spider_example.item_loaders import OfferLoader
from spider_example.items import Offer


class GetOffersSpider(scrapy.Spider):
    name = "get_offers"
    start_urls = [
        'https://ofertas.mercadolibre.com.ar/ofertas-de-la-semana',
    ]

    def parse(self, response):
        for item_info in response.css("div.item__info"):
            offer_loader = OfferLoader(Offer(), selector=item_info)
            offer_loader.add_css('description', "h2 span::text")
            offer_loader.add_css('price', "span.price__fraction::text")
            offer_loader.add_css('old_price', "span.price-old > del::text")
            offer_loader.add_css('discount', "div.item__discount::text")
            yield offer_loader.load_item()
        next_page_url = response.css("li.pagination__next > a::attr(href)").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))
