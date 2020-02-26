"""编写简单的登录界面"""

import tkinter as tk
from tkinter import messagebox


class Application(tk.Frame):
    '''简单的登录界面'''

    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        '''创建组件'''
        # 创建标签
        self.label01 = tk.Label(self,font=('黑体',10),text='用户名',width=10,height=2,bg='black',fg='white')
        self.label01.pack()
        # 创建输入框
        v1 = tk.StringVar()
        self.entry01 = tk.Entry(self,textvariable=v1)
        v1.set('admin')
        self.entry01.pack()

        # 创建标签
        self.label02 = tk.Label(self, font=('黑体', 10), text='密码', width=10, height=2, bg='black', fg='white')
        self.label02.pack()
        # 创建输入框
        v2 = tk.StringVar()
        self.entry02 = tk.Entry(self, textvariable=v2,show='*')
        self.entry02.pack()

        # 创建登录按钮
        global photo
        photo = tk.PhotoImage(file='img/start.gif')
        tk.Button(self,image=photo,command=self.login).pack()


    def login(self):
        '''送花'''
        username = self.entry01.get()
        passwd = self.entry02.get()
        # 比对用户名密码
        if username == 'admin' and passwd == 'nihao':
            messagebox.showinfo('提示', '用户{}登陆成功!'.format(self.entry01.get()))
        else:
            messagebox.showinfo('提示', '登陆失败!\n请检查用户名或密码！'.format(self.entry01.get()))


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('400x400+200+300')
    root.title('简单的登录界面')
    app = Application(master=root)
    root.mainloop()
