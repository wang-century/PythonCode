from multiprocessing import Queue, Process

"""
    multiprocessing模块的使用案例
Queue的常用方法
"""
# 创建队列
queue = Queue(3)  # 可以指定队列大小，默认无限
# 插入元素
queue.put('a')
queue.put('b')
queue.put('c')
# 判断队列是否已满
if queue.full():
    print('队列已满')
# 可选参数 block=True timeout=1 如果队列已满，等待1s，等待结束如果还是满的则抛出队列已满的异常
queue.put('d', block=True, timeout=1)
