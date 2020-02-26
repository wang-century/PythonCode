import requests
'''
    自定义requests请求类
'''

def get_response(url,headers=''):
    '''获取response响应'''
    response = requests.get(url,headers=headers).text
    return response


