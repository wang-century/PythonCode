# -*- coding: utf-8 -*-
"""
    抓取智联招聘大数据岗位信息  注：不可用（已过时）
"""
import requests
import json
import re
import threading
import pandas as pd
# from sqlalchemy import engine

# def save_to_mysql(data):
#     '''将数据保存到数据库'''
#     eng = engine.create_engine("mysql+pymysql://works:works@47.101.222.18:3306/works")
#     data = pd.DataFrame(data)
#     data.to_sql(name='java_works',con=eng,if_exists='replace')
#     print(data)

def save_data(filename,data):
    '''保存数据
    将数据转为json格式并保存
    :param filename: 文件名
    :param data: 数据
    :return: None
    '''
    print('保存文件{}.json中'.format(filename))
    with open(filename+'.json','w',encoding='utf-8') as f:
        #data = json.dumps(data)
        for d in data:
            #print(d)
            f.write(str(d)+'\n')
    print('保存文件{}.json完成'.format(filename))

def get_url_headers(url,page_count):
    '''根据页面数生成json数据url地址和headers请求头
    :param page_count: 页面数
    :return: url ：url地址
    '''
    if page_count == 0:
        # 生成url地址
        url = url[:35] + 'start={}&'.format(page_count) + url[35:]
    else:
        url = url[:35] + 'start={}&'.format(page_count * 90) + url[35:]
    # 生成headers
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Origin': 'https://sou.zhaopin.com',
        'Referer': 'https://sou.zhaopin.com/?p={}&jl=702&kw={}&kt=3&sf=0&st=0'.format(page_count,re.findall('&kw=(.*?)&kt',url)[0]),
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    return url,headers

def get_response(url,page_count):
    url,headers = get_url_headers(url,page_count)
    data = requests.get(url,headers=headers).text
    print(data)
    data = json.loads(data)
    null = None
    false = False
    true = True
    data1 = (data['data']['results'])
    job_info = []
    # “公司名称”、“工作城市”、“工作要求”、“招聘人数”、工资情况”（格式：‘底薪-上限’）、
    # “name”(岗位名称)、“detail”(职位详情)，
    for i in data1:
        job = {}
        # 工作名称
        job['jobName'] = i['jobName']
        job['salary'] = i['salary']
        job['welfare'] = ' '.join(i['welfare'])
        try:
            job['eduLevel'] = i['eduLevel']['name']
        except:
            job['eduLevel'] = '无要求'
        job['workingExp'] = ' '.join(i['workingExp']['name'])
        job['city'] = i['city']['display']
        job['require'] = i['company']['size']['name']
        job['company_name'] = i['company']['name']
        job_info.append(job)

    if len(job_info)>0:
        return job_info
    else:
        return None

def get_data(url,name):
    data = []
    count = 0
    while True:
        d = get_response(url,count)
        if d is None:
            print('数据采集完成')
            break
        data.extend(d)
        count += 1
    save_data(filename=name,data=data)


if __name__ == '__main__':
    urls = ['https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=702&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Python&kt=3&=0&_v=0.10086459&x-zp-page-request-id=6a89d831d31b4281b5923cb8d44f7707-1554795510384-844419',
            # 'https://fe-api.zhaopin.com/c/i/sou?start=90&pageSize=90&cityId=702&industry=160000&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E5%A4%A7%E6%95%B0%E6%8D%AE&kt=3&_v=0.67123213&x-zp-page-request-id=4bb01e76924c4edbab55d96c84c1be69-1559441041527-807008&x-zp-client-id=714b38e5-6e51-4cfa-a7d8-5e1d74e6438f',
            # 'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=538&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E5%A4%A7%E6%95%B0%E6%8D%AE&kt=3&_v=0.67123213&x-zp-page-request-id=4bb01e76924c4edbab55d96c84c1be69-1559441041527-807008&x-zp-client-id=714b38e5-6e51-4cfa-a7d8-5e1d74e6438f',
            'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=489&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E5%A4%A7%E6%95%B0%E6%8D%AE&kt=3&=0&_v=0.79460150&x-zp-page-request-id=c72aab2c5efe44c1b0f70958cc2536a5-1559442011459-268266&x-zp-client-id=714b38e5-6e51-4cfa-a7d8-5e1d74e6438f'
            ]
    t1 = threading.Thread(target=get_data(urls[1],name='Bigdata'),args=(1,))
    t1.start()