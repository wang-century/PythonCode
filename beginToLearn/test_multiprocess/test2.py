""" 多线程的简单使用
线程池的使用
"""
from multiprocessing import Pool
from time import sleep


def job(id):
    print('开始{}'.format(id))
    sleep(3)
    print('结束{}'.format(id))

if __name__ == '__main__':
    """进程池的使用（非阻塞）"""
    pool = Pool(processes=3)    # 创建线程池 线程数为3
    for i in range(5):
        # 执行的进程总数保持为3，只由当三个线程中有执行完毕的才添加新线程
        pool.apply_async(job,(i,))  # 传入的参数为：要执行的函数名  以及函数所需参数(元组)
    # 关闭线程池(不再接受新的线程请求)
    pool.close()
    # 注意：调用join之前需要先关闭线程池
    pool.join()     # join函数表示等待所有子进程结束
    """进程池的使用（阻塞）"""
    pool = Pool(processes=3)  # 创建线程池 线程数为3
    for i in range(5):
        # 执行的进程总数保持为3，只由当三个线程中有执行完毕的才添加新线程
        pool.apply(job, (i,))  # 传入的参数为：要执行的函数名  以及函数所需参数(元组)
    # 关闭线程池(不再接受新的线程请求)
    pool.close()
    # 注意：调用join之前需要先关闭线程池
    pool.join()  # join函数表示等待所有子进程结束

