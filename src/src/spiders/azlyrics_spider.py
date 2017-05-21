#!/usr/bin/python

import scrapy
from time import sleep

class AZLyricsSpider(scrapy.Spider):

    name = "AZLyricsSpider"
    domain = "http://www.azlyrics.com/"
    rotate_user_agent = True
    
    def start_requests(self):
        
        alphabets = "a"#bcdefghijklmnopqrstuvwxyz"
        url = "http://www.azlyrics.com/lyrics/aaronshust/godsolovedtheworld.html"
        yield scrapy.Request(url, callback=self.parse_lyrics)

        '''for alphabet in alphabets:
            url = self.domain + alphabet + ".html"
            yield scrapy.Request(url, callback=self.parse_artists)'''

    def parse_artists(self, response):
        
        print(response.url)
        for link in response.css('div.artist-col').css('a::attr(href)'):
            url = self.domain + link.extract()
            yield scrapy.Request(url, callback=self.parse_songs)

    def parse_songs(self, response):

        print(response.url)
        for link in response.xpath('//div[@id="listAlbum"]').css('a::attr(href)'):
            url = self.domain + link.extract()[3:]
            yield scrapy.Request(url, callback=self.parse_lyrics)

    def parse_lyrics(self, response):

        print(response.url)
        title = response.css('h1::text').extract_first()

        lyrics_div = response.css('div.text-center.col-xs-12.col-lg-8').css('div::text').extract()
        raw_lyrics = ''.join(lyrics_div).replace('\r\n', '\n')		
        while '\n\n\n' in raw_lyrics:
            raw_lyrics = raw_lyrics.replace('\n\n\n', '\n\n')
            lyrics = raw_lyrics

        txt = open(title+'.txt', 'w')
        txt.write(title+'\n')
        txt.write(lyrics)
        txt.close()
