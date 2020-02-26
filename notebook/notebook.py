"""记事本程序"""
from tkinter import Frame, Tk, Menu, Text
from tkinter.filedialog import askopenfilename


class Application(Frame):

    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.textpad = None     # Text文本框对象
        self.pack()
        self.createWidget()

    def createWidget(self):
        '''创建主内容'''
        # 创建主菜单
        menu_bar = Menu(root)

        # 创建子菜单
        menu_file = Menu(menu_bar)
        menu_edit = Menu(menu_bar)
        menu_help = Menu(menu_bar)

        # 将子菜单加到主菜单
        menu_bar.add_cascade(label='文件',menu=menu_file)
        menu_bar.add_cascade(label='编辑', menu=menu_edit)
        menu_bar.add_cascade(label='帮助', menu=menu_help)

        # 为文件子菜单添加菜单项
        menu_file.add_command(label="新建", accelerator="ctrl+n", command=self.test)
        menu_file.add_command(label="打开", accelerator="ctrl+o", command=self.open_file)
        menu_file.add_command(label="保存", accelerator="ctrl+s", command=self.test)
        menu_file.add_command(label="退出", accelerator="ctrl+q", command=self.test)

        # 主菜单添加到主窗口
        root['menu'] = menu_bar

        # 添加文本编辑区
        self.textpad = Text(root,width=50,height=30)
        self.textpad.pack()

        # 创建上下文菜单
        self.context_menu = Menu(root)
        self.context_menu.add_command(label='设置背景颜色',command=self.test)

        # 为上下文绑定事件（单机右键）
        root.bind('<Button-3>',self.create_context_menu)

    def open_file(self):
        """打开文件"""
        with open(askopenfilename(title='选择文件')) as f:
            self.textpad.insert(1.0, f.read())





    def create_context_menu(self,event):
        '''右键创建上下文菜单'''
        self.context_menu.post(event.x_root,event.y_root)



    def test(self):
        pass


if __name__ == '__main__':
    root = Tk()
    root.geometry("450x300+200+300")
    root.title("简易笔记本")
    app = Application(master=root)
    root.mainloop()