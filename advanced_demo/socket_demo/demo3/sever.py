from socket import *

# 创建服务器套接字对象
server_socket = socket(AF_INET,SOCK_STREAM)
# 绑定端口
server_socket.bind(('',9999))
# 监听
server_socket.listen()
# 接收客户端连接(获取客户端的socket和信息)
client_socket, client_info = server_socket.accept()
while True:
    # 接收客户端发送的消息
    receive_data = client_socket.recv(1024)
    print('接收数据：{}'.format(receive_data.decode()))
    # 发送消息
    message = input('>')
    if message == 'exit':
        break
    client_socket.send(message.encode('utf-8'))

# 关闭连接
client_socket.close()
server_socket.close()