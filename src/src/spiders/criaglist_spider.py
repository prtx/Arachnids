#!/usr/bin/python

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from src.items.craiglist_items import CraiglistItem

class CraigslistSpider(CrawlSpider):

    name = "CraigslistSpider"
    allowed_domains = ["criagslist.org"]
    start_urls = ["https://sfbay.craigslist.org/search/sof"]

    rules = Rule(
            LinkExtractor(
                allow = ("index\d00\.html"),
                ),
            callback = "parse_item",
            follow = True,
            ),

    def parse_items(self, response):

        hxs = Selector(response)
        results = hxs.xpath('//p')

        for result in results:

            item = CraiglistItem()

            item['title'] = result.xpath('a/text()').extract()
            item['link'] = result.xpath('a/@href').extract()
            item['datetime'] = result.xpath('time/@datetime').extract()
            item['location'] = result.xpath('span[@class="result-meta"]/span[@class="result-hood"]/text()').extract()

            yield item
