"""测试一个经典GUI程序写法，使用面向对象方式"""

import tkinter as tk
from tkinter import messagebox


class Application(tk.Frame):
    '''一个经典GUI程序的类写法'''

    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        '''创建组件'''
        # 创建标签
        self.label01 = tk.Label(self,font=('黑体',20),text='功能',width=10,height=2,bg='black',fg='white')
        self.label01.pack()
        # 创建送花按钮
        self.btn01 = tk.Button(self, text='点击送花', command=self.send_flower)
        self.btn01.pack()
        # 创建退出按钮
        self.quit_btn = tk.Button(self, text='退出', command=root.destroy)
        self.quit_btn.pack()
        # 显示图像
        global photo1    # 把photo声明成全局变量，如果是局部变量，本方法执行完毕后，图像对象销毁，窗口显示不出图像
        photo1 = tk.PhotoImage(file='img/logo.gif')  # 加载图片
        self.label02 = tk.Label(self,image=photo1)
        self.label02.pack()
        # 显示多行文本
        self.label04 = tk.Label(self,text='你是谁啊\n我是谁\n他是谁',borderwidth=5,relief='groove',justify='right')
        self.label04.pack()
        # 创建图像按钮
        global photo2
        photo2 = tk.PhotoImage(file='img/start.gif')
        self.start_btn = tk.Button(self,image=photo2,command=self.send_flower)
        self.start_btn.pack()


    def send_flower(self):
        '''送花'''
        messagebox.showinfo('提示', '送你花花')


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('400x400+200+300')
    root.title('经典GUI程序')
    app = Application(master=root)
    root.mainloop()
