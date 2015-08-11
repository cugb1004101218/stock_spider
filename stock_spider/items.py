# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class StockSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Stock(scrapy.Item):
  region = scrapy.Field()
  code = scrapy.Field()
  name = scrapy.Field()
