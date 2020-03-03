from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread


class ChatClient:
    """聊天程序客户端"""
    def __init__(self):
        """初始化"""
        self.client_socket = socket(AF_INET, SOCK_STREAM)       # 创建客户端套接字对象
        self.client_socket.connect(('172.26.100.112', 8888))     # 调用connect连接服务器
        thread1 = Thread(target=self.send_message, args=(self.client_socket,))  # 开启线程处理发送的数据
        thread2 = Thread(target=self.read_message, args=(self.client_socket,))  # 开启线程处理接收到的数据
        thread1.start()
        thread2.start()

    def send_message(self,client_socket):
        """发送消息"""
        while True:
            message = input('我:')
            client_socket.send(message.encode('utf-8'))

    def read_message(self, client_socket):
        """读取消息"""
        while True:
            receive_data = client_socket.recv(1024)  # 接收数据
            print('\n接收:{}'.format(receive_data.decode('utf-8')))  # 打印数据

    def __del__(self):
        self.client_socket.close()

if __name__ == '__main__':
    chat_client = ChatClient()