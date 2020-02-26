import scrapy
import pymongo

myclient = pymongo.MongoClient("mongodb://192.168.37.128:27017/")
mydb = myclient["books"]


class Books(scrapy.Spider):
    name = 'book2'
    start_urls = ['http://www.335xs.xyz/fenlei/6_2.html',
                  'http://www.335xs.xyz/fenlei/1_1.html',
                  'http://www.335xs.xyz/fenlei/2_1.html',
                  'http://www.335xs.xyz/fenlei/3_1.html',
                  'http://www.335xs.xyz/fenlei/4_1.html',
                  'http://www.335xs.xyz/fenlei/7_1.html',
                  'http://www.335xs.xyz/fenlei/10_1.html',
                  'http://www.335xs.xyz/fenlei/11_1.html']

    def parse(self, response):
        urls = response.xpath('//div[@id="alistbox"]//div[@class="yuedu"]/a[1]/@href').extract()
        for url in urls:
            yield scrapy.Request(url, callback=self.parse_book1)
        next_page_url = response.xpath('//a[@class="next"]/@href').extract_first()
        if next_page_url is not None:
            yield scrapy.Request(next_page_url, callback=self.parse)

    def parse_book1(self, response):
        item = {}
        item['type'] = response.xpath('//ul[@class="bread-crumbs"]/li[2]//text()').extract_first()
        item['name'] = response.xpath('//ul[@class="bread-crumbs"]/li[3]//text()').extract_first()
        mycol = mydb[item['type']]
        yes_or_no = False if len([i for i in mycol.find(item)]) > 0 else True
        if yes_or_no:
            content_url = 'http://www.335xs.xyz'+response.xpath('//span[@class="txtopt"]/a[1]/@href').extract_first()
            yield scrapy.Request(url=content_url,callback=self.parse_book2,meta=item)
        else:
            print(item['name']+'已存在')

    def parse_book2(self,response):
        meta = response.meta
        item = {}
        item['name'] = meta['name']
        item['type'] = meta['type']
        response = response
        item['content'] = response.body.decode('gb18030','ignore')
        # print(item)
        yield item

if __name__ == '__main__':
    import os
    os.system('scrapy crawl book2')



