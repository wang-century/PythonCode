"""
    pixiv爬虫
    说明：输入作者id，爬取该作者所有插画

    使用方法：首先在下面的username和passwd填写你的pixiv用户名和密码，然后等待selenium自动登录获取cookies，等待selenium关闭chrome浏览器后再命令行输入要抓取的作者id
    作者id获取示例： 点击作者头像 进入一个网页 该网页url于此类似 https://www.pixiv.net/users/6637740  则6637740为作者id

    注：该爬虫需要使用当前目录下的chromedriver.exe文件操作chrome浏览器；
        爬虫将使用chrome浏览器登录pixiv并获取cookies，请确保已安装chrome并且电脑可以直接访问pixiv


"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
import requests
from re import findall
from pathlib import Path
from os import mkdir

username = '1649601714@qq.com'   # 你的pixiv账号
passwd = 'wang2jing@'     # 你的pixiv密码·

class SpiderPixiv:
    """pixiv爬虫"""
    def __init__(self):
        """初始化爬虫"""
        self.get_cookies()  # 初始化requests对象
        self.get_author_id()  # 获取用户输入 插画作者id
        # 初始化创建图片保存文件夹
        try:
            mkdir('imgs')
        except Exception as e:
            print(e)

    def get_author_id(self):
        """获取用户输入 插画作者id"""
        self.author_id = input('请输入要抓取的作者id：')

    def get_cookies(self):
        """用于检测是否存在cookies文件（是则直接读取cookies，否则登录获取cookies并保存然后读取）"""
        try:

            self.read_cookies()
        except Exception:
            self.save_cookies()
            self.read_cookies()


    def save_cookies(self):
        """保存cookies到文件（不用每次爬取都登录一次）"""
        browser = webdriver.Chrome()  # 创建谷歌浏览器对象
        browser.get('https://accounts.pixiv.net/login')
        print('访问网址：{}访问网站标题：{}'.format(browser.current_url, browser.title))  # 打印网站网址和标题
        find_username_input = (By.XPATH, '//input[@autocomplete="username"]')
        # 找到并输入账号密码
        username_input = \
            WebDriverWait(browser, 10).until(expected_conditions.presence_of_all_elements_located(find_username_input))[
                0]
        username_input.send_keys(username)
        passwd_input = browser.find_element_by_xpath('//input[@autocomplete="current-password"]')
        passwd_input.send_keys(passwd)
        # 点击登录
        login_btn = browser.find_elements_by_xpath('//button[@class="signup-form__submit"]')[1]
        login_btn.click()
        # 获取cookies
        sleep(4)
        cookies = browser.get_cookies()
        browser.quit()  # 退出浏览器
        with open('pixiv_cookies.txt', 'w') as f:
            f.write(str(cookies))

    def read_cookies(self):
        """获取cookies并为request对象设置"""
        with open('pixiv_cookies.txt') as f:
            cookies = eval(f.read())
        # cookies = visit_pixiv() # 使用selenium模拟登陆获取cookies
        request_client = requests.Session()  # 创建request对象，用于爬虫使用
        # 为request对象设置cookies
        for cookie in cookies:
            request_client.cookies.set(cookie['name'], cookie['value'])
        request_client.headers.update({
            'authority': 'www.pixiv.net',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
        })
        self.requests = request_client

    def crawl_illustrations(self):
        """输入作者id获取该作者所有插画"""
        # 获取作者姓名
        index_url1 = 'https://www.pixiv.net/users/{}/illustrations'.format(self.author_id) # 根据作者id构建url
        content = self.requests.get(index_url1, headers={'referer': index_url1,
                                              'path': '/users/{}/illustrations'.format(self.author_id)}).text
        author_name = findall('<title>(.*?) - pixiv</title>',content)[0]
        # 创建该作者插画文件夹
        try:
            mkdir('imgs/{}'.format(author_name))
        except Exception as e:
            print(e)
        # 获取作者所有插画id
        index_url = 'https://www.pixiv.net/ajax/user/{}/profile/all'.format(self.author_id)
        response = self.requests.get(index_url,headers={'referer': index_url,'path': '/ajax/user/{}/profile/all'.format(self.author_id)}).text  # 获取网页响应
        response = eval(response.replace('false','False').replace('null','None').replace('true','True'))['body']['illusts']
        all_illusts = list(response.keys())
        illusts_count = len(all_illusts)
        print('该作者共有{}作品'.format(illusts_count))
        for i,illust_id in enumerate(all_illusts):
            print('正在保存id为{}的插画，总进度({}/{})'.format(illust_id,i+1,illusts_count))
            file_path = 'imgs/{}/{}.jpg'.format(author_name,illust_id)
            self.crawl_img(illust_id,file_path)

    def crawl_img(self,illust_id,file_path):
        """根据传入的插画id构建url获取插画地址"""
        # 检测插画是否已经存在，存在则跳过
        my_file = Path(file_path)
        if my_file.is_file():
            print('{}已下载'.format(file_path))
        else:
            page_url = 'https://www.pixiv.net/artworks/{}'.format(illust_id)
            response = self.requests.get(page_url, headers={'referer': page_url,'path':'/artworks/{}'.format(illust_id)}).text
            # 匹配图片地址
            result = findall(',"original":"(.*?)"},',response)[0]
            # 下载并写入文件
            with open(file_path,'wb') as f:
                f.write(self.requests.get(result, headers={'referer': page_url,'Sec-Fetch-Dest': 'image'}).content)
                print('{}保存完成'.format(file_path))
                sleep(2)

    def run(self):
        """运行"""
        self.crawl_illustrations()  # 抓取图片


if __name__ == '__main__':
    pixiv = SpiderPixiv()
    pixiv.run()
