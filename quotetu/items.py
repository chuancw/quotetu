# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# 需要爬取的字段
class QuotetuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    text = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()

