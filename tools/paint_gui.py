""" 使用tkinter实现简单画图软件 """
from tkinter import Frame, Tk, Menu, Text, END, messagebox, Canvas, Button
from tkinter.colorchooser import askcolor
from tkinter.filedialog import askopenfilename, asksaveasfilename

# 窗口设置
WIN_WIDTH = 900
WIN_HEIGHT = 450

class Application(Frame):
    """ 使用tkinter实现简单画图软件 """
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()
        self.bg_color = 'white' #'#000000'   # 背景颜色
        self.createWidget()

    def createWidget(self):
        """创建主内容"""
        # 创建绘图区域
        drawpad = Canvas(self.master,width=WIN_WIDTH,height=WIN_HEIGHT*0.9,bg=self.bg_color)
        drawpad.pack()

        # 创建工具按钮
        btn_start = Button(self.master,text='开始',name='start')  # 开始
        btn_start.pack(side='left',padx=10)     # 靠左 间距10
        btn_pen = Button(self.master, text='画笔', name='pen')    # 画笔
        btn_pen.pack(side='left', padx=10)
        btn_line = Button(self.master, text='直线', name='line')  # 直线
        btn_line.pack(side='left', padx=10)
        btn_line_arrow = Button(self.master, text='箭头直线', name='line_arrow')  # 带箭头直线
        btn_line_arrow.pack(side='left', padx=10)
        btn_rect = Button(self.master, text='矩形', name='rect')  # 矩形
        btn_rect.pack(side='left', padx=10)
        btn_clear = Button(self.master, text='清屏', name='clear')    # 清屏
        btn_clear.pack(side='left', padx=10)
        btn_eraser = Button(self.master, text='橡皮擦', name='eraser') # 橡皮擦
        btn_eraser.pack(side='left', padx=10)
        btn_color = Button(self.master, text='颜色', name='color')  # 颜色
        btn_color.pack(side='left', padx=10)







if __name__ == '__main__':
    root = Tk()
    root.geometry("{}x{}+200+300".format(WIN_WIDTH,WIN_HEIGHT))
    root.title("简易画图软件")
    app = Application(master=root)
    root.mainloop()
