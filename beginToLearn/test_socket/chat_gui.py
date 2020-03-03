from tkinter import Frame, Tk, Menu, Text, END, messagebox
from tkinter.colorchooser import askcolor
from tkinter.filedialog import askopenfilename, asksaveasfilename

class Application(Frame):
    """聊天程序图形化界面"""
    def __init__(self,master):
        super().__init__(master)
        self.master = master

    def create_widget(self):
        """设计界面"""


class Line1(Frame):
    """菜单栏"""
    def __init__(self,master):
        super().__init__(master)
        self.master = master

    def create_widget(self):
        """设计界面"""


if __name__ == '__main__':
    master = Tk()
    master.geometry("450x300+200+300")
    master.title("聊天程序")
    app = ChatApplication(master=master)
    master.mainloop()
