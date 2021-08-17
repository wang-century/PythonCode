from socket import *
from threading import Thread

"""udp实现聊天(多线程)"""

# 创建套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)
# 绑定端口
udp_socket.bind(('', 9998))  # 绑定本机端口9999
def receive_data():
    """接收数据"""
    while True:
        data = udp_socket.recvfrom(1024)  # 本次接收的最大字节数1024
        print('接收到[地址:{} 端口:{}]发送的消息:{}'.format(data[1][0], data[1][1], data[0].decode('utf-8')))


def send_data():
    """发送数据"""
    while True:
        message = input('(回车键发送数据)：')  # 要发送的数据
        address = ('localhost', 9999)  # 接收消息的地址
        # 发送消息
        udp_socket.sendto(message.encode('utf-8'), address)

if __name__ == '__main__':
    # 创建线程
    send_thread = Thread(target=send_data)
    receive_thread = Thread(target=receive_data)
    receive_thread.start()
    send_thread.start()
    receive_thread.join()
    send_thread.join()
