#!/usr/bin/python

import scrapy

class AZLyricsSpider(scrapy.Spider):
	
	name = "AZLyricsSpider"
	domain = "http://www.azlyrics.com/"


	def start_requests(self):
		
		alphabets = "a"#bcdefghijklmnopqrstuvwxyz"
		#url="http://www.azlyrics.com/a/augustburnsred.html"
		#yield scrapy.Request(url, callback=self.parse_songs)

		for alphabet in alphabets:
			url = self.domain + alphabet + ".html"
			yield scrapy.Request(url, callback=self.parse_artists)

	
	def parse_artists(self, response):
		
		for link in response.css('div.artist-col').css('a::attr(href)'):
			url = self.domain + link.extract()
			yield scrapy.Request(url, callback=self.parse_songs)
	
	
	def parse_songs(self, response):
		
		for link in response.xpath('//div[@id="listAlbum"]').css('a::attr(href)'):
			url = self.domain + link.extract()
			print(url)
