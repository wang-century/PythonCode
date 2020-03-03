""" 多线程的简单使用
使用队列实现进程之间的通信
注意；线程池使用队列与此不同
"""
from multiprocessing import Process,Queue
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
    que = Queue()   # 创建队列
    write_process = Process(target=write_queue,args=(que,)) # 创建写入线程
    read_process = Process(target=read_queue,args=(que,))   # 创建读取进程
    # 启动线程
    write_process.start()
    write_process.join()
    read_process.start()
    read_process.join()

