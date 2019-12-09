# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SimuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    MNGCNAME = scrapy.Field()
    REGISTDATE = scrapy.Field()
    MNGID = scrapy.Field()
    pass
