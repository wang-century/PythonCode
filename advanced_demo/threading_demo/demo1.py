from time import sleep
from threading import Thread, Lock

"""互斥锁的使用
注：线程之间资源共享
说明：在两个进程中都调用上锁的方法，那么两个线程会抢着上锁，如果一方上锁成功，另一方会阻塞到锁被解开
"""

money = 100  # 全局变量

lock = Lock()  # 创建互斥锁


def task1():
    global money
    for i in range(1000):
        lock.acquire()  # 上锁
        money += 1
        lock.release()  # 释放锁
    print('task1 money:{}'.format(money))


def task2():
    global money
    for i in range(10000):
        lock.acquire()  # 上锁
        money += 1
        lock.release()  # 释放锁
    print('task2 money:{}'.format(money))


if __name__ == '__main__':
    thread1 = Thread(target=task1)
    thread2 = Thread(target=task2)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
