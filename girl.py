# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import FemaleStarItem
import  re
class GirlSpider(CrawlSpider):
    name = 'girl'
    allowed_domains = ['win4000.com']
    start_urls = ['http://www.win4000.com/mt/star_1_2_1.html']

    rules = (
        Rule(LinkExtractor(allow=r'mt/star_1_2_\d.html'), follow=True), #列表页
        Rule(LinkExtractor(allow=r'mt/.+\.html',restrict_xpaths='//ul[@class="clearfix"]/li'),callback='parse_list_page', follow=False),
    )

    def parse_list_page(self, response):
        name=response.xpath('//div[contains(@class,"tit")]/h2/text()').get()
        name=name.split('图片')[0]
        alinks=response.xpath('//div[@class="tab_box"]/div/ul[@class="clearfix"]/li/a/img/@src').getall()
    # 删除不是以https开头无用的链接
        alinks=list(filter(lambda x:x.startswith('http'),alinks))
        image_urls=list(map(lambda x:re.sub(r"_250_300",'',x),alinks))


        item=FemaleStarItem(name=name,image_urls=image_urls)
        yield  item





