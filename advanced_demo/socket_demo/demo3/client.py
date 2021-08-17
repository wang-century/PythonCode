from socket import *

# 创建客户端套接字对象
client_socket = socket(AF_INET,SOCK_STREAM)
# 与服务器建立连接
client_socket.connect(('localhost',9999))
while True:
    # 发送消息
    message = input('>')
    if message == 'exit':
        break
    client_socket.send(message.encode('utf-8'))
    # 接收消息
    receive_data = client_socket.recv(1024)
    print('接收数据：{}'.format(receive_data.decode()))