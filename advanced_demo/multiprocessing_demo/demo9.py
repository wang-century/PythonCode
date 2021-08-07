from multiprocessing import Manager, Pool
from time import sleep

"""
    multiprocessing模块的使用案例
进程池内进程之间通信(Manager)
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
    q = Manager().Queue()  # 创建队列
    pool = Pool(2)  # 创建进程池
    # 创建进程
    pool.apply_async(write, (q,))
    pool.apply_async(read, (q,))
    pool.close()
    pool.join()
    print('主进程运行完毕')
