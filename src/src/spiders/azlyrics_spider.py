#!/usr/bin/python

import scrapy

class AZLyricsSpider(scrapy.Spider):
	
	name = "AZLyricsSpider"

	def start_requests(self):
		
		url = "http://www.azlyrics.com/a.html"
		#url = "http://quotes.toscrape.com/page/1/"

		yield scrapy.Request(url=url, callback=self.parse)

	
	def parse(self, response):
		
		for link in response.css('div.artist-col').css('a::attr(href)'):
			print(link.extract())
