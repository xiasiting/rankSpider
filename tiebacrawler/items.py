# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DetailItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    reply = scrapy.Field()

class RankingRecord(scrapy.Item):
    worldrank = scrapy.Field()
    institution = scrapy.Field()
    Country_Reg = scrapy.Field()
    NationalRank = scrapy.Field()
    totalscore = scrapy.Field()
    alumni = scrapy.Field()
    award = scrapy.Field()
    hici = scrapy.Field()
    n_s = scrapy.Field()
    pub = scrapy.Field()
    pcp = scrapy.Field()