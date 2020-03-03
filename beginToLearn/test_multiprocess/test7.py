""" 多线程的简单使用
使用_thread模块
"""
from _thread import start_new_thread
from time import sleep


def job1(name,sleep_time):
    print('开始运行{}'.format(name))
    sleep(sleep_time)
    print('{}运行结束'.format(name))

def job2(name,sleep_time):
    print('开始运行{}'.format(name))
    sleep(sleep_time)
    print('{}运行结束'.format(name))

if __name__ == '__main__':
    print('主线程运行')
    # 启动线程运行函数
    start_new_thread(job1,('线程1',2))
    start_new_thread(job2,('线程2',3))
    sleep(6)