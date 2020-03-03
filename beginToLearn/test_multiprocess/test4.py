""" 多线程的简单使用
队列的简单使用
"""

from multiprocessing import Queue

# 创建队列
que = Queue(4)  # 参数为队列容量，默认无限

# 向队列中放置内容
que.put('内容1')
que.put('内容2')
que.put('内容3')
que.put('内容4')
# print('队列是否已满：',que.full())
# que.put('内容5',timeout=3)  # 因为队列已满，所以内容5无法放置    设置超时 若超过设置的时间仍未放置则报出异常“queue.Full”
print('队列是否已满：', que.full())
# 可以在写入时先判断队列是否已满,若未满则放入
if not que.full():
    que.put('内容5')
# 所以在读取队列时需要先判断队列是否为空,不为空则读取
if not que.empty():
    for i in range(que.qsize()):
        print(que.get())
