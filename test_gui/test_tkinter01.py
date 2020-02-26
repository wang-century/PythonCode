from tkinter import *
from tkinter import messagebox

root = Tk()  # 创建窗口

root.title('第一个GUI程序')  # 设置窗口标题

root.geometry('500x300+100+200')    # 宽度 * 高度 + 距屏幕左边缘  + 距屏幕上边缘

btn01 = Button(root)  # 创建按钮对象，放置到root窗口
btn01['text'] = '点我送花'

btn01.pack()  # 合理放置按钮


def send_flower(e):
    ''' 送花
        e是事件对象 '''
    messagebox.showinfo('Message', '送你花')  # 显示消息框，参数为标题及内容


btn01.bind('<Button-1>', send_flower)  # 绑定事件

if __name__ == '__main__':
    root.mainloop()  # 调用组件的mainloop()方法，进入事件循环
