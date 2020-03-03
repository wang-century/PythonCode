""" 网络编程
    TFTP文件下载器
"""

"""示例：TFTP文件下载客户端"""
from struct import pack,unpack
from socket import *

file_name = 'face.jpg'  # 要下载的文件名称
server_ip = '127.0.0.1'  # 下载的目标服务器ip地址
send_data = pack('!H{}sb5sb'.format(len(file_name)),1,file_name.encode(),0,'octet'.encode(),0)  # 向服务器发送的数据
s = socket(AF_INET,SOCK_DGRAM)  # 创建socket
s.sendto(send_data,(server_ip,69))  # 发送数据
file = open(file_name,'ab') # 以追加方式打开，二进制
while True:
    receive_data = s.recvfrom(1024) # 接收数据  1024为最大数据量
    i,j = unpack('!HH',receive_data[0][:4]) # 获取数据块编号
    rand_port = receive_data[1][1]  # 获取服务器随机端口

    if int(i) == 5:
        print('文件不存在')
        break
    print('操作码：{},ACK：{},服务器随机端口：{},数据长度：{}'.format(i,j,rand_port,len(receive_data[0])))
    file.write(receive_data[0][4:]) # 向文件写入数据
    if len(receive_data[0]) < 516:
        break
    ack_data = pack('!HH',4,j)
    s.sendto(ack_data,(server_ip,rand_port))    # 发送ACK确认包