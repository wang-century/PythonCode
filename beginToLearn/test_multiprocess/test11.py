""" 多线程的简单使用(threading模块)
    线程同步的使用
    如：线程A与B配合，A执行到某一步需要B的某个结果，示意B运行，B运行后将结果给A，A继续执行
    本例中首先对lock2和lock3上锁，所以在三个线程开始后，Task2和Task3由于上锁状态无法执行，首先执行Task1，在执行时先为lock1上锁，执行语句后将
    lock2改为未锁定状态，运行Task2，在执行Task2时为lock2上锁，执行语句后释放lock3，然后Task3执行...
所以运行结果为：运行Task1 --> 运行Task2 --> 运行Task3 --> 运行Task1 --> 运行Task2 --> 运行Task3 ...
"""
from time import sleep
from threading import Thread,Lock

# 创建锁
lock1 = Lock()
lock2 = Lock()
lock3 = Lock()
# 为lock2和lock3上锁
lock2.acquire()
lock3.acquire()

class Task1(Thread):
    def run(self):
        while True:
            if lock1.acquire():
                print('运行Task1')
                sleep(1)
                lock2.release()

class Task2(Thread):
    def run(self):
        while True:
            if lock2.acquire():
                print('运行Task2')
                sleep(1)
                lock3.release()

class Task3(Thread):
    def run(self):
        while True:
            if lock3.acquire():
                print('运行Task3')
                sleep(1)
                lock1.release()

if __name__ == '__main__':
    t1 = Task1()
    t2 = Task2()
    t3 = Task3()
    t1.start()
    t2.start()
    t3.start()


