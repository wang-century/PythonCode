

import tkinter as tk
from tkinter import messagebox, HORIZONTAL
from tkinter.colorchooser import askcolor
from tkinter.filedialog import askopenfilename, askopenfile


class Application(tk.Frame):
    '''GUI的简单测试'''

    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.master = master
        self.pack()
        self.createWidget()
        self.createWidget2()

    def createWidget(self):
        """单选按钮、复选按钮、下拉选项、移动滑块"""
        # 创建单选按钮
        self.v = tk.StringVar()
        self.v.set('F')
        self.r1 = tk.Radiobutton(self, text='男', value='M', variable=self.v)
        self.r2 = tk.Radiobutton(self, text='女', value='F', variable=self.v)
        self.r1.pack(side='left')
        self.r2.pack(side='left')
        # 创建多选按钮
        self.code_hobby = tk.IntVar()
        self.video_hobby = tk.IntVar()
        self.c1 = tk.Checkbutton(self, text='敲代码', variable=self.code_hobby, onvalue=1, offvalue=0)
        self.c2 = tk.Checkbutton(self, text='看电影', variable=self.video_hobby, onvalue=1, offvalue=0)
        self.c1.pack(side='left')
        self.c2.pack(side='left')

        # 下拉选项
        self.label1 = tk.Label(self,text='选择职业')
        self.label1.pack()
        self.d = tk.StringVar()
        self.d.set('程序员')
        self.menu = tk.OptionMenu(self,self.d,'程序员','厨师','家教')
        self.menu['width'] = 10
        self.menu.pack()

        # 创建滑块
        self.scale1 = tk.Scale(self,from_=10,to=50,length=200,tickinterval=5,orient=tk.HORIZONTAL,command=self.set_font)
        self.scale1.pack()
        self.label2 = tk.Label(self,text='滑块控制大小')
        self.label2.pack()

        tk.Button(self, text='确定', command=self.confirm).pack(side='left')

    def createWidget2(self):
        '''创建颜色框、文件选择框、读取文件内容'''
        # 颜色框
        self.btn1 = tk.Button(self,text='选择背景色',command=self.ask_color).pack()
        # 文件选择框
        self.label3 = tk.Label(self,text='请选择文件',justify='left')
        self.label3.pack()
        self.label4 = tk.Label(self,text='该处显示文件内容',justify='left')
        self.label4.pack()
        self.btn2 = tk.Button(self,text='选择文件',command=self.choose_file)
        self.btn2.pack()

    def choose_file(self):
        '''选择文件'''
        filename = askopenfilename(title='选择文件')#,filetypes=[('视频文件','.mp4')])#initialdir='')
        print(filename)
        self.label3['text'] = filename
        self.label4['text'] = askopenfile(title='选择文件').read()





    def ask_color(self):
        '''调出颜色选择框'''
        s1 = askcolor(color='red',title='选择背景色')
        self.master.config(bg=s1[1])
        self.config(bg=s1[1])



    def confirm(self):
        messagebox.showinfo('提示', '所选内容:\n单选：{}\n多选：{}，{}\n下拉选项：{}'.format(self.v.get(), self.code_hobby.get(), self.video_hobby.get(),self.d.get()))

    def set_font(self,size):
        '''通过滑块值设定字体大小'''
        print('滑块值：{}'.format(size))
        self.label2.config(font=('宋体',size))


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('400x400+200+300')
    root.title('单选按钮、复选按钮、下拉选项、移动滑块')
    app = Application(master=root)
    root.mainloop()
