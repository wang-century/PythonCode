import requests
from lxml.etree import HTML
import redis

class MeiZiSpider:
    '''爬虫爬取妹子图'''
    def __init__(self):
        self.index_url = 'https://www.mzitu.com/'
        self.redis_cli = redis.Redis(host='localhost', port=6379, decode_responses=True)


    def get_response(self, url):
        '''获取网页内容'''
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
            'authority': 'www.mzitu.com'}
        response = requests.get(url,headers=headers).text
        return HTML(response)

    def crawl_one_page(self,url):
        '''抓取某一页内所有套图url并存放到redis集合,并返回下一页地址'''
        response = self.get_response(url)
        content = response.xpath('//ul[@id="pins"]//li')
        for con in content:
            url = con.xpath('./a/@href')
        next_url = response.xpath('//a[text()="下一页»"]/@href')
        if next_url:
            return next_url
        else:
            return None

    def run(self):
        '''主函数，运行爬虫'''
        print('请输入运行的模式：\n1.爬取妹子图并上传url到redis队列\n2.从redis队列爬取图片到本地')
        next_url = self.crawl_one_page(self.index_url)
        while next_url is not None:
            next_url = self.crawl_one_page(self.index_url)




if __name__ == '__main__':
    meizi = MeiZiSpider()
    meizi.run()