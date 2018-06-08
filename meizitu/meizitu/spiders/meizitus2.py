# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import MeizituItem


class Meizitus2Spider(CrawlSpider):
    name = 'meizitus2'
    allowed_domains = ['www.mzitu.com']
    start_urls = ['http://www.mzitu.com/']

    rules = (
        # Rule(LinkExtractor(allow=r'http://www.mzitu.com/page/\d+/'), callback='parse_item', follow=True),
        # Rule(LinkExtractor(allow=r'http://www.mzitu.com/xinggan/'), callback='parse_item', follow=True),
        # Rule(LinkExtractor(allow=r'http://www.mzitu.com/xinggan/page/\d+/'), callback='parse_item', follow=True),
        # Rule(LinkExtractor(allow=r'http://www.mzitu.com/japan/(.*?)/'), callback='parse_item', follow=True),
        # Rule(LinkExtractor(allow=r'http://www.mzitu.com/taiwan/(.*?)/'), callback='parse_item', follow=True),
        # Rule(LinkExtractor(allow=r'http://www.mzitu.com/mm/(.*?)/'), callback='parse_item', follow=True),
        # Rule(LinkExtractor(allow=r'http://www.mzitu.com/mm/(.*?)/'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'http://www.mzitu.com/(.*?)/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i
        photo_list = response.xpath('//ul[@id="pins"]/li')
        for li in photo_list:
            item = MeizituItem()
            photo = li.xpath('.//a/img/@data-original').extract_first()
            title = li.xpath('.//span/a/text()').extract_first()
            item['photo'] = photo
            item['title'] = title
            yield item


