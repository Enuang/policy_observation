# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GdspiderItem(scrapy.Item):
    title = scrapy.Field()
    time = scrapy.Field()
    link = scrapy.Field()
    #pass


class DetailsItem(scrapy.Item):
    detail = scrapy.Field()
