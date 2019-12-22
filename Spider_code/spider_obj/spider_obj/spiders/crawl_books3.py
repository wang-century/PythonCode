import scrapy
import pymongo

myclient = pymongo.MongoClient("mongodb://192.168.37.128:27017/")
mydb = myclient["books"]


class Books(scrapy.Spider):
    name = 'book3'
    start_urls = ['http://www.kwt.one/fenlei/10_1/']

    def parse(self, response):
        content = response.xpath('//div[@id="container"]//div[@class="box"]')
        for con in content[:1]:
            meta = {}
            url = con.xpath('./a[1]/@href').extract_first()
            meta['type'] = response.xpath('//div[@class="layout-hd"]/h2/text()').extract_first()
            meta['name'] = con.xpath('.//a[@class="booktitle"]/text()').extract_first()
            yield scrapy.Request(url=url,callback=self.parse_book1,meta=meta)
        # 进入下一页
        next_page_url = response.xpath('//a[@class="next"]/@href').extract_first()
        if next_page_url is not None:
            yield scrapy.Request(next_page_url, callback=self.parse)

    def parse_book1(self, response):
        '''进入章节目录'''
        chapters_page_url = response.xpath('//a[@class="catalogbtn"]/@href').extract_first()
        yield scrapy.Request(chapters_page_url,callback=self.parse_book2,meta=response.meta)

    def parse_book2(self,response):
        '''获取所有章节内容'''
        meta = response.meta
        content = response.xpath('//div[@class="chapter-con"]//li//a')
        for con in content:
            url = con.xpath('./@href').extract_first()
            name = con.xpath('./text()').extract_first()
            meta['name'] = name
            # 检测文章是否已存在
            mycol = mydb[meta['type']]
            yes_or_no = False if len([i for i in mycol.find(meta)]) > 0 else True
            if yes_or_no:
                yield response.follow(url=url,callback=self.parse_book3,meta=meta)
            else:
                print(meta['name'] + '已存在')


    def parse_book3(self,response):
        item = {}
        item['name'] = response.meta['name']
        item['type'] = response.meta['type']
        item['content'] = '\n'.join(response.xpath('//div[@class="article-con"]//text()').extract())
        yield item



if __name__ == '__main__':
    import os
    os.system('scrapy crawl book3')



