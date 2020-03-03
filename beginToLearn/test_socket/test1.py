""" 网络编程
    测试UDP发送与接收数据
"""

from socket import socket,AF_INET,SOCK_DGRAM

def use_udp_send_data():
    """使用UDP发送数据"""
    s = socket(AF_INET,SOCK_DGRAM)  # 创建UDP套接字
    address = ('172.26.100.112',8080)    # 接收方地址
    send_data = input('请输入要发送的数据：')
    s.sendto(send_data.encode('gbk'),address)   # 发送数据时需要将字符串转成byte，编码格式为gbk
    s.close()   # 关闭套接字

def use_udp_send_receive_data():
    """使用UDP发送与接收数据"""
    s = socket(AF_INET,SOCK_DGRAM)
    s.bind(('',8788)) # 绑定一个地址(即ip与端口号，ip一般不用写)
    address = ('172.26.100.112',8080)    # 接收方地址
    send_data = input('请输入要发送的数据：')
    s.sendto(send_data.encode('gbk'), address)  # 发送数据时需要将字符串转成byte，编码格式为gbk
    receive_data = s.recvfrom(1024) # 1024为本次接收的最大字节数
    print('接收到数据：{}'.format(receive_data[0].decode('gbk')))
    s.close()

if __name__ == '__main__':
    use_udp_send_receive_data()