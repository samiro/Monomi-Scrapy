from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from monomi.items import MonomiItem

class MonomiSpider(BaseSpider):
    name = "monomi"
    allowed_domains = ["monomi.co"]
    url = "http://fsh-store.monomi.co"
    start_urls = [
        url + "/products/"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        products = hxs.select('//ul[@id="product-list"]/li')
        items = []
        for prod in products:
            item = MonomiItem()
            item['name'] = prod.select('div[@class="product_small_view"]/div[@class="info"]/h3/a/text()').extract()
            item['price'] = prod.select('div[@class="product_small_view"]/div[@class="info"]/p/a/text()').extract()
            item['img'] = [self.url + str(e) for e in prod.select('div[@class="product_small_view"]/a[@class="image"]/img/@src').extract()]
            item['url'] = [self.url + str(e) for e in prod.select('div[@class="product_small_view"]/div[@class="info"]/h3/a/@href').extract()]
            items.append(item)
        return items