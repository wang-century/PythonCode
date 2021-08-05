from multiprocessing import Process
from time import sleep

"""
    multiprocessing模块的使用案例
创建带参和不带参子进程
"""


def task():
    """不带参任务"""
    print('任务一子进程调用')
    print('任务一子进程调用结束')


def task2(name, **kwargs):
    """带参任务"""
    print('参数kwargs:', kwargs)
    for i in range(5):
        print('子进程{}, 输出:{}'.format(name, i))
        sleep(0.5)


if __name__ == '__main__':
    print('主进程运行')
    process = Process(target=task)  # 创建不带参子进程
    process2 = Process(target=task2, args=('任务二',), kwargs={'age': 13})  # 创建带参子进程
    print('子进程将要执行')
    process2.start()
    process.start()
    print('主进程运行完毕')
