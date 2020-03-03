"""
    使用TCP模拟QQ聊天（一问一答）
"""
from socket import *

def server_machine():
    """服务器端"""
    # 创建服务器端套接字对象
    server_socket = socket(AF_INET,SOCK_STREAM)
    # 绑定端口
    server_socket.bind(('',8888))
    # 监听
    server_socket.listen()
    # 等待客户端连接
    client_socket,client_info = server_socket.accept()
    while True:
        # 接收客户端消息
        receive_data = client_socket.recv(1024)
        print('{}:{}'.format(client_info,receive_data.decode('uft-8')))
        # 发送消息
        message = input('我:')
        client_socket.send(message.encode('utf-8'))

def client_machine():
    """客户端"""
    # 创建服务器端套接字对象
    client_socket = socket(AF_INET, SOCK_STREAM)
    # 与服务器建立连接
    client_socket.connect(('172.26.100.112',8888))
    while True:
        # 客户端发送消息
        message = input('我:')
        client_socket.send(message.encode('uft-8'))
        # 接收消息
        receive_data = client_socket.recv(1024)
        print('服务器端:{}'.format(receive_data.decode('utf-8')))

