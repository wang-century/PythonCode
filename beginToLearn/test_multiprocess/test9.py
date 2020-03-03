""" 多线程的简单使用
在threading模块 线程之间共享全局变量
注：在一个进程内所有线程共享全局变量，多线程之间的数据共享比多进程好，但是可能造成多个进程同时修改一个变量，造成混乱
"""
from threading import Thread


COUNT = 0  # 设置全局变量COUNT


def add_number1(num):
    """修改全局变量"""
    global COUNT
    print('add_number1')
    COUNT += num
    print(COUNT)


def add_number2(num):
    """修改全局变量"""
    global COUNT
    print('add_number2')
    COUNT += num
    print(COUNT)


if __name__ == '__main__':
    p = Thread(target=add_number1, args=(3,))
    p.start()
    p.join()
    p = Thread(target=add_number2, args=(4,))
    p.start()
    p.join()
    print('最终结果：COUNT={}'.format(COUNT))