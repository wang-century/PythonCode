import scrapy

myclient = pymongo.MongoClient("mongodb://192.168.37.128:27017/")
mydb = myclient["books"]


class Books(scrapy.Spider):
    name = 'meizitu'
    start_urls = ['https://www.mzitu.com/']

    def parse(self, response):
        content = response.xpath('//ul[@id="pins"]//li')
        for con in content:
            url = con.xpath('./a/@href').extract_first()

        next_page_url = response.xpath('//a[@title="下一页"]/@href').extract_first()
        if next_page_url is not None:
            yield scrapy.Request('https://www.ahk85.com' + next_page_url, callback=self.parse)

    def parse_img(self, response):
        item = {}
        content = response.xpath('//div[@class="content"]//p//text()').extract()
        item['content'] = '\n'.join(content)
        item['type'] = response.xpath('//div[@class="row nav-row"]//a[last()-1]/text()').extract_first()
        item['name'] = meta['name']
        yield item
