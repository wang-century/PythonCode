""" 网络编程
    TCP服务器端接收数据
"""

from struct import pack,unpack
from socket import *

server_socket = socket(AF_INET,SOCK_STREAM) # 创建socket
server_socket.bind(('',8899))   # 绑定端口
server_socket.listen(5) # 设置最大等待数
client_socket,client_info = server_socket.accept()  # 获取客户端socket以及客户端信息
receive_data = client_socket.recv(1024) # 获取客户端请求数据
print('{}:{}'.format(str(client_info),receive_data.decode('gbk')))
client_socket.close()
server_socket.close()