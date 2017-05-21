#!/usr/bin/python

import scrapy
from src.items.pokemondb_items import PokemonItem
from time import sleep

class PokemonDBSpider(scrapy.Spider):

    name = "PokemonDBSpider"
    rotate_user_agent = True
    
    def start_requests(self):
        
        url = "https://pokemondb.net/pokedex/all"
        yield scrapy.Request(url, callback=self.parse_pokedex)


    def parse_pokedex(self, response):
        
        table_rows = response.xpath('//table[@id="pokedex"]/tbody/tr')
        for row in table_rows:

            pokemon = PokemonItem()

            pokemon['no'] = row.xpath('td[1]/text()').extract_first()
            pokemon['name'] = row.xpath('td[2]/a/text()').extract_first()
            pokemon['pokemon_type'] = row.xpath('td[3]/a/text()').extract()
            pokemon['total'] = row.xpath('td[4]/text()').extract_first()
            pokemon['hp'] = row.xpath('td[5]/text()').extract_first()
            pokemon['attack'] = row.xpath('td[6]/text()').extract_first()
            pokemon['defense'] = row.xpath('td[7]/text()').extract_first()
            pokemon['special_attack'] = row.xpath('td[8]/text()').extract_first()
            pokemon['special_defense'] = row.xpath('td[9]/text()').extract_first()
            pokemon['speed'] = row.xpath('td[10]/text()').extract_first()

            yield pokemon
