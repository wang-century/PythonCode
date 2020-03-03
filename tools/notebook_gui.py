"""使用tkinter实现简单记事本程序"""
from tkinter import Frame, Tk, Menu, Text, END, messagebox
from tkinter.colorchooser import askcolor
from tkinter.filedialog import askopenfilename, asksaveasfilename


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.textpad = None  # Text文本框对象
        self.open_file_name = None  # 用于判断是否已经打开文件
        self.pack()
        self.createWidget()

    def createWidget(self):
        '''创建主内容'''
        # 创建主菜单
        menu_bar = Menu(self.master)

        # 创建子菜单
        menu_file = Menu(menu_bar)
        menu_edit = Menu(menu_bar)
        # menu_help = Menu(menu_bar)    # 帮助菜单 (未实现)

        # 将子菜单加到主菜单
        menu_bar.add_cascade(label='文件', menu=menu_file)
        menu_bar.add_cascade(label='编辑', menu=menu_edit)
        # menu_bar.add_cascade(label='帮助', menu=menu_help)

        # 为文件子菜单添加菜单项
        menu_file.add_command(label="新建", accelerator="ctrl+n", command=self.create_file)
        menu_file.add_command(label="打开", accelerator="ctrl+o", command=self.open_file)
        menu_file.add_command(label="保存", accelerator="ctrl+s", command=self.save_file)
        menu_file.add_separator()  # 添加分割线
        menu_file.add_command(label="退出", accelerator="ctrl+q", command=self.exit)

        # 为编辑子菜单添加选项
        menu_edit.add_command(label="设置文字颜色", command=self.set_font_color)
        menu_edit.add_command(label="设置背景颜色", command=self.set_bg_color)

        # 主菜单添加到主窗口
        self.master['menu'] = menu_bar

        # 添加文本编辑区
        self.textpad = Text(self.master, width=70, height=30)
        self.textpad.pack()

        # 创建上下文(右键)菜单
        self.context_menu = Menu(self.master)
        self.context_menu.add_command(label='设置文字颜色', command=self.set_font_color)
        self.context_menu.add_command(label='设置背景颜色', command=self.set_bg_color)

        # 为上下文绑定事件（单机右键）
        self.master.bind('<Button-3>', self.create_context_menu)

        # 增加快捷键的处理
        self.master.bind("<Control-n>", lambda event: self.create_file())
        self.master.bind("<Control-o>", lambda event: self.open_file())
        self.master.bind("<Control-s>", lambda event: self.save_file())
        self.master.bind("<Control-q>", lambda event: self.exit())

    def open_file(self):
        """打开文件"""
        self.textpad.delete("1.0", "end")  # 把text控件中所有的内容清空
        self.open_file_name = askopenfilename(title='选择文件')
        with open(self.open_file_name) as f:
            self.textpad.insert(1.0, f.read())

    def create_file(self):
        """新建文件"""
        self.textpad.delete("1.0", "end")  # 把text控件中所有的内容清空
        try:
            self.filename = asksaveasfilename(title="另存为", initialfile="未命名.txt",
                                              filetypes=[("文本文档", "*.txt")],
                                              defaultextension=".txt")
            with open(self.filename, 'w') as f:
                f.write(self.textpad.get(1.0, END))
            self.open_file_name = self.filename  # 将打开的文件名设置为新建的文件名!
        except Exception as e:
            print(e)

    def save_file(self):
        """保存文件"""
        text_content = self.textpad.get(1.0, END)
        if self.open_file_name is not None:
            with open(self.open_file_name, 'w') as f:
                f.write(text_content)
                messagebox.showinfo('提示', '保存成功！')
        else:
            self.create_file()

    def exit(self):
        """退出程序"""
        quit = messagebox.askquestion('退出', '是否退出？')
        if quit == 'yes':
            self.master.destroy()

    def create_context_menu(self, event):
        '''右键创建上下文菜单'''
        self.context_menu.post(event.x_root, event.y_root)

    def set_bg_color(self):
        """设置背景颜色"""
        color = askcolor(color='red', title='选择背景色')
        self.textpad.config(bg=color[1])

    def set_font_color(self):
        """设置文字颜色"""
        color = askcolor(color='red', title='选择背景色')
        self.textpad.config(fg=color[1])


if __name__ == '__main__':
    root = Tk()
    root.geometry("450x300+200+300")
    root.title("简易笔记本")
    app = Application(master=root)
    root.mainloop()
