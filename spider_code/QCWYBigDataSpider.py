"""
    爬取前程无忧大数据职位信息并保存到csv文件
    例：{'work_name': '大数据开发工程师', 'company_name': '加东信息科技（深圳）有限公司', 'work_exp': '3-4年经验', 
        'edu_level': '本科', 'work_require_people': '招2人', 'release_time': '06-19发布', 'work_location': '深圳-福田区', 
        'salary': '2-2.5万/月', 'company_type': '外资（非欧美）', 'company_size': '150-500人', 'company_industry': '酒店/旅游 计算机软件'}
"""

import requests
from lxml import etree
# from pymongo import MongoClient

class WuyouSpider:
    def __init__(self):
        '''初始化'''
        # 职位链接url地址 从1开始
        self.url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,%25E5%25A4%25A7%25E6%2595%25B0%25E6%258D%25AE,2,{}.html'
        self.file = open('qiancheng.csv','w',encoding='utf-8')
        # 连接mongodb数据库
        # mongo = MongoClient(host='localhost',port=27017)
        # db = mongo['qianchengwuyou']
        # self.cursor = db['wuyou']
        self.file.write('{},{},{},{},{},{},{},{},{},{},{}\n'.format('work_name','company_name','edu_level','work_require_people','work_exp','release_time',
            'work_location','salary','company_type','company_size','company_industry'))
        

    def get_response(self,url):
        '''获取response响应'''
        headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"
        }
        response = requests.get(url,headers=headers)
        response.encoding = 'gbk'
        return response.text

    def parse_list(self,data):
        '''处理数据，消除列表符号'''
        return ''.join(data)



    def parse_work_info(self,url):
        '''根据职位链接获取职位信息'''
        response = self.get_response(url)
        html_content = etree.HTML(response)
        #  工作年限要求，学历要求，招聘人数  职能类别
        work = {}
        #  职位名称（岗位名称）、公司名称、 工作地点、薪资（底薪-上限）、发布时间（月-日）；
        work['work_name'] = self.parse_list(html_content.xpath("//div[@class='in']/div[@class='cn']/h1/@title"))
        work['company_name'] = self.parse_list(html_content.xpath("//div[@class='in']/div[@class='cn']/p[@class='cname']/a/@title"))
        # 结果为一串字符，需要进行分割 并去除空字符
        content1 = self.parse_list(html_content.xpath("//div[@class='in']/div[@class='cn']/p[@class='msg ltype']/@title")).split('|')
        content1 = [i.strip() for i in content1]
        # 提取结果 ['广州-天河区', '5-7年经验', '本科', '招1人', '06-03发布']
        for con in content1:
            if con in ['初中及以下','高中/中技/中专','本科','无工作经验',' 大专']:
                work['edu_level'] = con
            if con.find('招') != -1:
                work['work_require_people'] = con
            if con.find('经验') != -1:
                work['work_exp'] = con
            if con.find('发布') != -1:
                work['release_time'] = con
        for column in ['edu_level','work_require_people','work_exp','release_time']:
            if column not in work.keys():
                work[column] = None
        work['work_location'] = content1[0]
        work['salary'] = self.parse_list(html_content.xpath("//div[@class='in']/div[@class='cn']/strong/text()"))
        # 公司性质  公司规模（人数）  公司所属行业
        work['company_type'] = self.parse_list(html_content.xpath("//div[@class='com_tag']/p[1]/@title"))
        work['company_size'] = self.parse_list(html_content.xpath("//div[@class='com_tag']/p[2]/@title"))
        work['company_industry'] = self.parse_list(html_content.xpath("//div[@class='com_tag']/p[3]/@title")).replace(',',' ')
        print(work)
        # 将数据写入mongodb数据库
        # self.cursor.insert_one(work) 
        
        
        # 将数据写入csv
        self.file.write('{},{},{},{},{},{},{},{},{},{},{}\n'.format(work.get('work_name') or '空',work.get('company_name') or '空',work.get('edu_level') or '空',work.get('work_require_people') or '空',work.get('work_exp') or '空',
                                                        work.get('release_time') or '空',work.get('work_location') or '空',work.get('salary') or '空',work.get('company_type') or '空',work.get('company_size') or '空',work.get('company_industry') or '空'))
        if len(work) < 2:
            return False
        else:
            return True


    def parse_page_href(self,page):
        '''获取页面内职位链接
        参数:   page  页数(从1开始)
        '''
        url = self.url.format(page)
        response = self.get_response(url)
        html_content = etree.HTML(response)
        # 提取链接
        works_url = html_content.xpath("//div[@class='dw_table']//div[@class='el']/p/span/a/@href")

        
                
        # 根据职位链接获取职位信息
        for url in works_url:
            resu = self.parse_work_info(url)
            if resu is False:
                print('爬取结束')
                return False
        

    def run(self):
        '''爬取前程无忧大数据相关岗位招聘信息
        步骤：
            1.获取第一页所有职位链接
            2.根据职位链接获取职位信息
            3.获取下一页职位链接
            4.根据职位链接获取职位信息...
        '''
        # 1.获取第一页所有职位链接
        page = 1
        # while 循环中的page用于控制爬取页面数 此处小于三页
        while page<3:
            resu = self.parse_page_href(page)
            if resu is False:
                break 
            page += 1
        self.file.close()


if __name__ == '__main__':
    wuyou = WuyouSpider()
    wuyou.run()