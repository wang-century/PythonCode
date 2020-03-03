""" 多线程的简单使用
子进程之间数据不共享
"""
from multiprocessing import Process

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
    p = Process(target=add_number1, args=(3,))
    p.start()
    p.join()
    p = Process(target=add_number2, args=(4,))
    p.start()
    p.join()
    print('最终结果：COUNT={}'.format(COUNT))
