import requests
from lxml.etree import HTML

index_url = 'http://www.335xs.xyz'


def get_response(url):  # 获取response
    response = requests.get(url,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'})
    response.encoding = 'gbk'
    return response.text

def get_page_book_list(response): # 获取一个页面内的所有图书url
    result = response.xpath('//div[@id="alistbox"]//div[@class="yuedu"]/a[1]/@href')
    print(result)
    return result

def get_next_page(response):    # 获取下一页地址
    result = response.xpath('//a[@class="next"]/@href')
    print(result)
    return result

def run1(url):
    response = HTML(get_response(url))
    book_list = get_page_book_list(response)
    for i in book_list:
        download_url = index_url+HTML(get_response(i)).xpath('//span[@class="txtopt"]/a[1]/@href')[0]
        print(get_response(download_url))
    #next_url = get_next_page(response)


def run2():
    request_url = 'http://www.335xs.xyz/fenlei/6_1.html'
    run1(request_url)


if __name__ == '__main__':
    run2()