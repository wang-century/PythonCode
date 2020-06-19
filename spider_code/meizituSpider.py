""" 爬虫爬取妹子图
    可选爬取的页面范围
    妹子类型
    1.https://www.mzitu.com/xinggan/ 性感妹子
    2.https://www.mzitu.com/japan/ 日本妹子
    3.https://www.mzitu.com/taiwan/ 台湾妹子
    4.https://www.mzitu.com/mm/ 清纯妹子
"""

from os import mkdir
from os.path import exists
import requests
from lxml.etree import HTML
from time import sleep


class MeiziSpider:
    def __init__(self):
        """ 爬虫初始化：
            1.妹子图地址
            1.创建图片保存目录
        """
        self.index_url_list = ['https://www.mzitu.com/xinggan/','https://www.mzitu.com/japan/','https://www.mzitu.com/taiwan/','https://www.mzitu.com/mm/']
        # 创建图片保存目录
        self.folder_name = '妹子图'
        try:  # 添加错误机制，防止文件存在导致运行错误
            mkdir(self.folder_name)
        except:
            pass

    def get_response(self, url, referer=None, host=None):
        """获取网页响应"""
        headers = {
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8,ru;q=0.7,und;q=0.6',
            'Connection': 'keep-alive',
            'Host': host,
            'Referer': referer,
            'Sec-Fetch-Dest': 'image',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Site': 'cross-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
        }
        response = requests.get(url=url, headers=headers)
        response.encoding = 'UTF-8'
        return response

    def save_img(self, url, save_path):
        """保存图片"""
        response = HTML(self.get_response(url, referer=url).text)
        name = response.xpath('//h2[@class="main-title"]/text()')[0]  # 获取套图名称
        img_url = response.xpath('//div[@class="main-image"]/p/a/img/@src')[0]  # 获取该页图片地址
        img_name = '{}/{}'.format(save_path, name + '.jpg')
        # 判断图片是否存在，存在则跳过，不存在则下载
        if exists(img_name) is True:
            print('{}已存在'.format(img_name))
        else:
            with open(img_name, 'wb') as f:  # 请求图片url获取图片内容并保存图片
                f.write(self.get_response(img_url, referer=url, host='i5.mmzztt.com').content)
                print('已保存{}'.format(img_name))
                sleep(0.5)  # 设置延时，防止高频次导致的问题
        next_page_url = response.xpath('//a[span[text()="下一页»"]]/@href'.format(name))
        if len(next_page_url) > 0:
            self.save_img(next_page_url[0], save_path)
        else:
            print('套图{}爬取完成'.format(save_path))

    def crawl_one_page(self, url):
        '''抓取一页内所有套图url，并获取下一页地址 递归调用自身'''
        response = HTML(self.get_response(url, referer=url).text)
        content = response.xpath('//ul[@id="pins"]//li')
        for con in content:
            url = con.xpath('./a/@href')[0]  # 获取套图url
            name = con.xpath('./a/img/@alt')[0]  # 获取套图名称，为套图创建文件夹
            save_path = '{}/{}'.format(self.folder_name, name)
            try:
                mkdir(save_path)
            except:
                pass
            print('正在爬取{}'.format(save_path))
            self.save_img(url, save_path=save_path)  # 根据套图url获取所有图片并保存
            sleep(5)
        # 抓取下一页地址 若不存在则程序退出
        next_url = response.xpath('//a[text()="下一页»"]/@href')
        if len(next_url) > 0:
            self.crawl_one_page(next_url[0])
        else:
            print('程序结束')

    def run(self):
        """运行"""
        type_choice = int(input('抓取妹子图请\n类型：1.性感妹子\t2.日本妹子\t3.台湾妹子\t4.清纯妹子\t0.退出\n选择抓取的类型：'))
        if type_choice == 0:
            return True
        try:
            crawl_url = self.index_url_list[type_choice-1]
            response = HTML(self.get_response(url=crawl_url).text)
            total_page = response.xpath('//div[@class="nav-links"]//a[last()-1]/text()')[0]  # 获取总页数
            choice = input('当前共{}页套图，请选择要爬取的页数(范围1-{})：\n示例：3-5爬取3页到5页的内容(包括3,5)\n'.format(total_page, total_page))
            start_page = int(choice.split('-')[0])
            end_page = int(choice.split('-')[1])
        except Exception as e:
            print('输入错误{}'.format(e))
        else:
            crawl_page_list = ['https://www.mzitu.com/xinggan/page/{}/'.format(i) for i in
                               range(start_page, end_page + 1)]
            for url in crawl_page_list:
                self.crawl_one_page(url=url)



if __name__ == '__main__':
    meizi = MeiziSpider()
    meizi.run()
