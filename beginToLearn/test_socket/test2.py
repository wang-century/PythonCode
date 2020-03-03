""" 网络编程
    使用多线程、UDP实现聊天
"""

from socket import socket,AF_INET,SOCK_DGRAM
from threading import Thread

udp_socket = socket(AF_INET,SOCK_DGRAM)     # 创建socket
udp_socket.bind(('',8989))      # 绑定端口

def receive_data():
    """接收数据"""
    while True:
        data = udp_socket.recvfrom(1024)   # 1024为本次接收的最大字节数
        print('\n来自{}:{}'.format(data[1],data[0].decode('gbk')))

def send_data():
    """发送数据"""
    while True:
        address = ('172.26.100.112', 8080)  # 接收方地址
        data = input('请输入要发送的数据：')
        udp_socket.sendto(data.encode('gbk'), address)  # 发送数据时需要将字符串转成byte，编码格式为gbk

if __name__ == '__main__':
    t1 = Thread(target=send_data)
    t2 = Thread(target=receive_data)
    t1.start()
    t2.start()
    t1.join()
    t2.join()