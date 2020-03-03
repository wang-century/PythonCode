""" 多线程的简单使用
使用队列实现进程池中进程之间的通信
"""
from multiprocessing import Process,Pool,Manager
from time import sleep

def write_queue(que):
    """将列表元素写入队列"""
    for i in ['你','好','啊']:
        print('开始写入:',i)
        que.put(i)
        sleep(1)

def read_queue(que):
    """从队列中读取元素"""
    print('开始读取')
    while True:
        if not que.empty():
            print('读取元素:',que.get())
        else:
            break

if __name__ == '__main__':
    que = Manager().Queue() # 创建队列
    # 创建进程
    pool = Pool(2)
    pool.apply(write_queue,(que,))
    pool.apply(read_queue,(que,))
    pool.close()
    pool.join()