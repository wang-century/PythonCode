import multiprocessing.pool
from time import sleep

"""
    multiprocessing模块的使用案例
进程池的使用(非阻塞)
"""


def task(name, sleep_time):
    """任务"""
    print('任务{}开始执行'.format(name))
    sleep(sleep_time)
    print('任务{}结束执行'.format(name))


if __name__ == '__main__':
    print('主进程运行')
    pool = multiprocessing.Pool(processes=2)  # 创建进程池，同时运行的进程个数为2
    # 创建5个进程并交给pool执行
    for i in range(5):
        pool.apply_async(task, ('任务{}'.format(i), 2))
    # 关闭线程池，线程池关闭后不再接受新的请求
    pool.close()
    # 等待所有子进程结束
    pool.join()
    print('主进程运行完毕')
