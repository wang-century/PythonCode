from multiprocessing import Process
from time import sleep

"""
    multiprocessing模块的使用案例
使用继承方式创建进程(继承Process类，重写run方法)
"""


class MyProcess(Process):
    def __init__(self, name, sleep_time):
        super().__init__()
        self.sleep_time = sleep_time
        self.name = name

    def run(self):
        print('进程{}开始执行')
        sleep(self.sleep_time)
        print('进程{}结束执行')


if __name__ == '__main__':
    print('主进程运行')
    process = MyProcess('测试进程一', 2)
    process.start()
    process.join()
    print('主进程运行完毕')
