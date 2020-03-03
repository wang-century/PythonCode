""" 多线程的简单使用
创建子进程并调用
"""
from multiprocessing import Process
from time import sleep

def job(sleep_tine):
    """设定任务"""
    print('job工作开始')
    sleep(sleep_tine)   # 等待
    print('job工作结束')

if __name__ == '__main__':
    # 1. 主进程不等待子进程执行完毕
    print('主进程开始')
    j = Process(target=job,args=(2,))   # 创建Process对象，设定延时2秒
    j.start()   # 开始进程
    print('主进程结束')
    # 2. 主进程等待子进程执行完毕
    print('主进程开始')
    j = Process(target=job, args=(2,))  # 创建Process对象，设定延时2秒
    j.start()  # 开始进程
    j.join()    # 添加此语句  表示等待进程j终止
    print('主进程结束')
    # 3. 主进程等待子进程一定事件后，若子进程仍未执行完毕，则继续执行主进程
    print('主进程开始')
    j = Process(target=job, args=(2,))  # 创建Process对象，设定延时2秒
    j.start()  # 开始进程
    j.join(timeout=1)  # 添加timeout参数表示等待进程j的时间
    print('打印进程信息：\n进程pid：{},进程名称：{},进程是否存活：{}'.format(j.pid,j.name,j.is_alive()))
    print('主进程结束')


