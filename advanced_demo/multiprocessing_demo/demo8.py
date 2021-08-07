from multiprocessing import Process, Queue
from time import sleep

"""
    multiprocessing模块的使用案例
多进程之间通信(Queue)
"""


def write(q):
    """将元素写入队列"""
    for i in ['a', 'b', 'c', 'd']:
        print('向队列写入{}'.format(i))
        q.put(i)
        sleep(1)


def read(q):
    """从队列读取元素"""
    while True:
        if not q.empty():
            print('从队列读取{}'.format(q.get()))
            sleep(1)
        else:
            break


if __name__ == '__main__':
    print('主进程运行')
    q = Queue()  # 创建队列
    process1 = Process(target=write, args=(q,))
    process2 = Process(target=read, args=(q,))
    process1.start()
    process2.start()
    process1.join()
    process2.join()
    print('主进程运行完毕')
