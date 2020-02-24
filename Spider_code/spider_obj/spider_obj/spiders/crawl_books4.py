import scrapy
import pymongo

myclient = pymongo.MongoClient("mongodb://172.26.78.4:27017/")
mydb = myclient["books"]

index_url = "https://m.xiaoqiangwx.org/"

class Books(scrapy.Spider):
    name = 'book4'
    start_urls = ['https://m.xiaoqiangwx.org/sort-5-1/']

    def parse(self, response):
        content = response.xpath('//div[@class="cover"]//p/a[2]')
        for con in content:
            href = index_url + con.xpath('./@href').extract_first()
            yield scrapy.Request(url=href,callback=self.parse_book1)
    #     # 进入下一页
    #     next_page_url = response.xpath('//a[@class="next"]/@href').extract_first()
    #     if next_page_url is not None:
    #         yield scrapy.Request(next_page_url, callback=self.parse)
    #
    def parse_book1(self, response):
        '''进入章节目录'''
        chapters_page_url = index_url + response.xpath('//a[text()="查看目录"]/@href').extract_first()
        yield scrapy.Request(chapters_page_url,callback=self.parse_book2)

    def parse_book2(self,response):
        '''获取所有章节'''
        content = response.xpath('//ul[@class="chapter"]//li//a')
        for con in content:
            url = index_url + con.xpath('./@href').extract_first()
            yield scrapy.Request(url, callback=self.parse_book3)
        next_page_url = response.xpath('//a[text()="下一页"]/@href').extract_first()
        if next_page_url:
            yield scrapy.Request(index_url + next_page_url, callback=self.parse_book2)

    def parse_book3(self,response):
        '''获取章节内所有页面内容'''
        item = {}
        item['title'] = response.xpath('//h1/text()').extract_first()
        item['name'] = response.xpath('//div[@class="nr_title"]/text()').extract_first()
        item['content'] = '\n'.join(response.xpath('//div[@id="nr"]//text()').extract())
        yield item
        next_page_url = response.xpath('//a[text()="下一页"]/@href').extract_first()
        if next_page_url:
            yield scrapy.Request(index_url + next_page_url, callback=self.parse_book3)

if __name__ == '__main__':
    import os
    os.system('scrapy crawl book4 -o book.csv')



