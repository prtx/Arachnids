# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PokemonItem(scrapy.Item):
    
    no = scrapy.Field()
    name = scrapy.Field()
    pokemon_type = scrapy.Field()
    total = scrapy.Field()
    hp = scrapy.Field()
    attack = scrapy.Field()
    defense = scrapy.Field()
    special_attack = scrapy.Field()
    special_defense = scrapy.Field()
    speed = scrapy.Field()
