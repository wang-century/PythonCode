from distutils.core import setup

setup(
    name = 'centurysRequests',  # 我们模块的名字
    version='1.0', #版本号
    description = '自定义requests工具，测试用',  # 描述
    author='centuryw', #作者
    author_email = 'wsj@centuryw.cn', # 作者邮箱
    py_modules = ['centurysRequests.requests']  # 要发布的模块
)

import centurysRequests.requests