from socket import socket, AF_INET, SOCK_DGRAM

"""udp发送数据"""

# 创建套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)
message = '测试数据'  # 要发送的数据
address = ('localhost', 9999)  # 接收消息的地址
# 发送消息
udp_socket.sendto(message.encode('utf-8'), address)
# 关闭套接字
udp_socket.close()
