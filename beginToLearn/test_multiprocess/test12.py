""" 多线程的简单使用(threading模块)
    生产者-消费者模式
    使用队列，生产者将产品放入队列，消费者直接从队列中取出产品
"""
from time import sleep
from threading import Thread
from queue import Queue

class Producer(Thread):
    """生产者"""
    def run(self):
        global queue
        count = 0
        while True:
            # 判断队列的大小
            if queue.qsize()<1000:
                for i in range(100):
                    count += 1
                    message = '生产产品：'+str(count)
                    print(message)
                    queue.put('产品{}'.format(count))
                sleep(0.5)

class Consumer(Thread):
    """消费者"""
    def run(self):
        global queue
        while True:
            if queue.qsize()>100:
                for i in range(10):
                    message = self.name+'消费：'+queue.get()
                    print(message)
                sleep(1)



if __name__ == '__main__':
    queue = Queue() # 创建队列
    p = Producer()  # 创建生产者
    p.start()   # 运行生产者
    sleep(1)
    c = Consumer()  # 创建消费者
    c.start()




