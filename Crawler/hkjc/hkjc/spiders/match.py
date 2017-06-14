# -*- coding: utf-8 -*-
import scrapy


class MatchSpider(scrapy.Spider):
    name = 'match'
    allowed_domains = ['bet.hkjc.com']
    start_urls = ['http://bet.hkjc.com/football/getXML.aspx?pooltype=HAD']
    
    def parse(self, response):
        matches = response.xpath('//MATCH')
        
        for index, match in enumerate(matches):
            pool = match.xpath('POOL')
            args = (match.xpath('@ID').extract(), pool.xpath('@A').extract(), pool.xpath('@D').extract(), pool.xpath('@H').extract())
            print(args)
