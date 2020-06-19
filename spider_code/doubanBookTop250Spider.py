"""
    爬取豆瓣图书Top250
    注：爬取图书信息并以字典形式保存到json文件
    例：{'name': '目送', 'date': ' 2009-10 ', 'price': ' 39.00元', 'press': ' 生活·读书·新知三联书店 ', 'author': '龙应台 '}
"""

import requests
from lxml import etree
from time import sleep
import json

def get_response(url):
    '''
    获取response相应内容
    :param url:
    :return: response
    '''
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"
    }
    response = requests.get(url,headers=headers).text
    return response

def handel_html(response):
    '''
    将response转为HTML
    :param response:
    :return:
    '''
    html = etree.HTML(response)
    return html

def save_to_file(filename,data):
    '''
    将数据保存到json文件
    :param data:
    :return: None
    '''
    data = json.dumps(data)

    with open(filename,'w') as f:
        f.write(str(data))
        print('保存完成，文件为',filename)


def handel_page_data(response):
    '''
    使用xpath解析网页，获取图书信息
    :param response: 网页响应内容
    :return:page_books： 该页所有图书信息
    '''
    # 保存该页所有图书信息
    page_books = []
    # 每个图书信息分别保存在 class="indent" 的div下的 table标签内
    book_table =  handel_html(response).xpath('//div[@class="indent"]//table')
    for book_td in book_table:
        # 保存单个图书信息
        book = {}
        # 图书名保存在 class="pl2" 的div下的第一个 a标签内的title属性内
        book['name'] = book_td.xpath('.//div[@class="pl2"]//a[1]/@title')[0]
        # 图书 作者、图书价格、出版日期、出版社保存再 class="pl" 的 p标签下
        other_info = book_td.xpath('.//p[@class="pl"]/text()')[0]
        # 分割字符串
        other_info = other_info.split('/')
        # 价格索引为-1 出版日期-2 出版社-3 作者[:-3]
        book['date'] = other_info[-2]
        book['price'] = other_info[-1]
        book['press'] = other_info[-3]
        # 去除author的中括号
        book['author'] = other_info[:-3]
        book['author'] = ' '.join(book['author'])
        print(book)
        # 放入该页所有图书信息
        page_books.append(book)
    return page_books

def get_next_url(response):
    '''
    使用xpath解析网页，获取下一页url地址
    :param response: 网页响应内容
    :return: next_url :下一页url地址
    '''
    # 下一页地址保存再 text()='后页>' 中的 a标签的href属性
    html = handel_html(response)
    next_url = html.xpath('//a[text()="后页>"]/@href')
    # 如果下一页链接存在
    if len(next_url)>0:
        return next_url[0]
    else:
        return None

def run():
    '''
    豆瓣图书top250  爬取 图书名、作者、图书价格、出版日期、出版社、评分、评价人数、引语
    主函数
    1.获取首页response响应
    2.解析网页内容，获取所需信息 (使用xpath解析)
    3.循环获取下一页url
        获取下一页response响应
        解析网页内容，获取所需信息
    6.保存到文件     json格式：[ {bookname: name , author: author, book_price:price ... },...  ]
    :return:None
    '''
    # 用于保存所有图书信息
    books_info = []
    index_url = 'https://book.douban.com/top250?icn=index-book250-all'
    # 1.获取首页response响应
    response = get_response(index_url)
    # 2.解析网页内容，获取所需信息 (使用xpath解析)
    page_books = handel_page_data(response)
    print(page_books)
    # 放入所有图书信息中
    books_info.extend(page_books)
    # 3.获取下一页url
    next_url = get_next_url(response)
    # 当下一页存在
    while next_url is not None:
        # 设置延时4秒 防止封ip
        sleep(2)
        # 1.获取首页response响应
        response = get_response(next_url)
        # 2.解析网页内容，获取所需信息 (使用xpath解析)
        page_books = handel_page_data(response)
        print(page_books)
        # 放入所有图书信息中
        books_info.extend(page_books)
        # 3.获取下一页url
        next_url = get_next_url(response)
    print('数据获取完毕，共%d条'%len(books_info))
    print('正在保存数据')
    save_to_file(filename='data.json',data=books_info)



if __name__ == '__main__':
    run()