from multiprocessing import Process

"""
    multiprocessing模块的使用案例
多进程之间数据不共享
"""

money = 100


def task1():
    global money
    money += 2000
    print('task1 money:{}'.format(money))   # 2100

def task2():
    global money
    money += 10000
    print('task2 money:{}'.format(money))   # 10100


if __name__ == '__main__':
    print('主进程运行')
    process1 = Process(target=task1)
    process2 = Process(target=task2)
    process1.start()
    process2.start()
    process1.join()
    process2.join()
    print('主进程 money:{}'.format(money)) # 100
    print('主进程运行完毕')
