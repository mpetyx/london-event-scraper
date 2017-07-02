from __future__ import absolute_import

from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity
from scrapy.spiders import Rule

from ..utils.spiders import BasePortiaSpider
from ..utils.starturls import FeedGenerator, FragmentGenerator
from ..utils.processors import Item, Field, Text, Number, Price, Date, Url, Image, Regex
from ..items import PortiaItem


class Skiddle(BasePortiaSpider):
    name = "skiddle"
    allowed_domains = [u'www.skiddle.com']
    start_urls = [u'https://www.skiddle.com/whats-on/London/']
    rules = [
        Rule(
            LinkExtractor(
                allow=('.*'),
                deny=()
            ),
            callback='parse_item',
            follow=True
        )
    ]
    items = [
        [
            Item(
                PortiaItem, None, '', [
                    Field(
                        u'image', '', []), Field(
                        u'title', '', []), Field(
                            u'location', '', []), Field(
                                u'date', '', [])])]]
