from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

class ChatServer:
    """聊天程序服务器端"""

    def __init__(self):
        """初始化"""
        self.server_socket = socket(AF_INET, SOCK_STREAM)    # 创建服务器端socket
        self.server_socket.bind(('',8888))   # 绑定端口
        self.server_socket.listen()  # 监听
        self.receive_client()   # 开始接收客户端请求


    def receive_client(self):
        """接收客户端请求"""
        while True:
            client_socket, client_info = self.server_socket.accept()
            print('{}已连接'.format(client_info))
            # 开启线程处理当前客户端请求
            thread1 = Thread(target=self.read_message,args=(client_socket,))
            thread1.start()
            # 创建线程发送数据
            thread2 = Thread(target=self.send_message, args=(client_socket,))
            thread2.start()



    def read_message(self,client_socket):
        """读取消息"""
        while True:
            receive_data = client_socket.recv(1024) # 接收客户端数据
            print('\n接收:{}'.format(receive_data.decode('utf-8')))  # 打印数据


    def send_message(self,client_socket):
        """发送消息"""
        while True:
            message = input('我:')
            client_socket.send(message.encode('utf-8'))




if __name__ == '__main__':
    char_server = ChatServer()  # 创建服务器对象
