# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImdbItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    pass

class MoviesItem(scrapy.Item):
    rank = scrapy.Field()
    title = scrapy.Field()
    year = scrapy.Field()
    duration = scrapy.Field()
    genre = scrapy.Field()
    rating = scrapy.Field()
    vote = scrapy.Field()
    gross = scrapy.Field()
    description = scrapy.Field()