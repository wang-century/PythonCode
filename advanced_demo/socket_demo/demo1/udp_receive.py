from socket import *

"""udp接收数据"""

# 创建套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)
# 绑定端口
udp_socket.bind(('', 9999))  # 绑定本机端口9999
# 接收数据
data = udp_socket.recvfrom(1024)  # 本次接收的最大字节数1024
# print(data)  # (b'\xe6\xb5\x8b\xe8\xaf\x95\xe6\x95\xb0\xe6\x8d\xae', ('127.0.0.1', 53255))
# print(data[0].decode('utf-8'))  # 测试数据
print('接收到[地址:{} 端口:{}]发送的消息:{}'.format(data[1][0], data[1][1], data[0].decode('utf-8')))
# 关闭套接字
udp_socket.close()
