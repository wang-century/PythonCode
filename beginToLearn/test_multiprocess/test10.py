""" 多线程的简单使用
在threading模块 线程之间共享全局变量
注：在一个进程内所有线程共享全局变量，多线程之间的数据共享比多进程好，但是可能造成多个进程同时修改一个变量，造成混乱
    为了防止混乱，需要使用 “ 互斥锁 ”
锁有两种状态：锁定和未锁定。某个线程要更改共享数据时，要先将其锁定，其它线程不能更改，直到该线程释放资源，将其状态变为非锁定，其它线程才能锁定并修改数据
"""
from threading import Thread, Lock

COUNT = 0  # 设置全局变量COUNT
lock_count = Lock()  # 创建互斥锁


def add_number1():
    """修改全局变量"""
    global COUNT
    print('add_number1')
    for i in range(10000):
        lock_count.acquire()  # 上锁
        COUNT += 1
        lock_count.release()    # 解锁
    print(COUNT)


def add_number2():
    """修改全局变量"""
    global COUNT

    print('add_number2')
    for i in range(10000):
        lock_count.acquire()  # 上锁
        COUNT += 1
        lock_count.release()  # 解锁
    print(COUNT)


if __name__ == '__main__':
    p = Thread(target=add_number1, args=())
    p.start()
    p.join()
    p = Thread(target=add_number2, args=())
    p.start()
    p.join()
    print('最终结果：COUNT={}'.format(COUNT))
