#!/usr/bin/python

from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from src.items.craiglist_items import CraiglistItem

class CraigslistSpider(BaseSpider):

    name = "CraigslistSpider"
    allowed_domains = ["criagslist.org"]
    start_urls = ["https://sfbay.craigslist.org/search/sof"]

    def parse(self, response):

        hxs = Selector(response)
        results = hxs.xpath('//p')

        for result in results:

            item = CraiglistItem()

            item['title'] = result.xpath('a/text()').extract()
            item['link'] = result.xpath('a/@href').extract()
            item['datetime'] = result.xpath('time/@datetime').extract()
            item['location'] = result.xpath('span[@class="result-meta"]/span[@class="result-hood"]/text()').extract()

            yield item
