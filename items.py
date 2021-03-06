# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class MeituzzItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class MeituItem(scrapy.Item):
    _id = Field()
    key = Field()
    link = Field()

class ImageItem(scrapy.Item):
    image_urls = Field()
    albumID = Field()
    image_paths = Field()
