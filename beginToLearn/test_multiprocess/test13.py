""" 多线程的简单使用(threading模块)
    ThreadLocal的使用
    ThreadLocal本身是一个全局变量，但是每个线程却可以利用它来保存属于自己的私有数据，这些私有数据对其他线程也是不可见的。
"""
from threading import Thread,local,current_thread

local = local()

def process_student():
    student_name = local.name   # 获取当前线程关联的name
    print('线程名：{}\t学生名：{}'.format(current_thread().name,student_name))

def process_thread(name):
    local.name = name   # 绑定ThreadLocal的名称
    process_student()

if __name__ == '__main__':
    t1 = Thread(target=process_thread,args=('小七',),name='线程A')
    t2 = Thread(target=process_thread,args=('小六',),name='线程B')
    t1.start()
    t2.start()
    t1.join()
    t2.join()


