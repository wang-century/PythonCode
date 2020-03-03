""" 多线程的简单使用
使用threading模块
    threading.currentThread()   返回当前的线程变量
    threading.enumerate()       返回一个包含正在运行的线程list
    threading.activeCount()     返回正在运行的线程数量
    Thread(group=None.target=None,name=None,args=(),kwargs={})  # 创建线程
"""
from threading import Thread
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
    print('主进程运行')
    # 创建线程
    t1 = Thread(target=job1,args=('线程1',2))
    t2 = Thread(target=job2,args=('线程2',1))
    t1.start()
    t2.start()
    t1.join()
    t2.join()