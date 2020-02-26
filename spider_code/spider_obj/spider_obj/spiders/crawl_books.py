import scrapy
import pymongo

myclient = pymongo.MongoClient("mongodb://192.168.37.128:27017/")
mydb = myclient["books"]


class Books(scrapy.Spider):
    name = 'book'
    start_urls = ['https://www.ahk85.com/xiaoshuo/list-%E5%AE%B6%E5%BA%AD%E4%B9%B1%E4%BC%A6.html',
                  'https://www.ahk85.com/xiaoshuo/list-%E9%83%BD%E5%B8%82%E6%BF%80%E6%83%85.html',
                  'https://www.ahk85.com/xiaoshuo/list-%E4%BA%BA%E5%A6%BB%E4%BA%A4%E6%8D%A2.html',
                  'https://www.ahk85.com/xiaoshuo/list-%E6%A0%A1%E5%9B%AD%E6%98%A5%E8%89%B2.html',
                  'https://www.ahk85.com/xiaoshuo/list-%E5%8F%A6%E7%B1%BB%E5%B0%8F%E8%AF%B4.html'
                  ]

    def parse(self, response):
        content = response.xpath('//div[@class="text-list-html"]//ul//li//a[@title]')
        for con in content:
            item = {}
            item['name'] = con.xpath('./@title').extract_first()
            item['type'] = response.xpath('//div[@class="row nav-row"]//a[last()]/text()').extract_first()
            mycol = mydb[item['type']]
            yes_or_no = False if len([i for i in mycol.find(item)]) > 0 else True
            if yes_or_no:
                item['href'] = 'https://www.ahk85.com' + con.xpath('./@href').extract_first()
                yield scrapy.Request(item['href'], callback=self.parse_book, meta=item)
        next_page_url = response.xpath('//a[@title="下一页"]/@href').extract_first()
        if next_page_url is not None:
            yield scrapy.Request('https://www.ahk85.com' + next_page_url, callback=self.parse)

    def parse_book(self, response):
        meta = response.meta
        item = {}
        content = response.xpath('//div[@class="content"]//p//text()').extract()
        item['content'] = '\n'.join(content)
        item['type'] = response.xpath('//div[@class="row nav-row"]//a[last()-1]/text()').extract_first()
        item['name'] = meta['name']
        yield item
