''' 使用tkinter+百度ocr实现简单文字识别程序
    这里用的是我个人的APP设置，可以自行去申请（免费）
    详情请看我写的教程 https://centurye.com/?p=1140 或视频 https://www.bilibili.com/video/av54709168
    或直接百度
'''
from tkinter import Frame,Button,Label,Text,END,Tk
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo
from aip import AipOcr


class BaiduOcr():
    '''百度OCR文字识别'''
    def __init__(self):
        """初始化连接"""
        APP_ID = '11386043'
        API_KEY = 'GhRCZnOKIqs6x76osXqZxGM9'
        SECRET_KEY = 'OLEhkqKpjknGzYtPeu0g4I46FRdXBb2m'
        self.client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    def return_result(self,filePath):
        '''获取识别结果'''
        # 读取图片
        with open(filePath, 'rb') as fp:
            image_file = fp.read()
        # 调用通用文字识别, 图片参数为本地图片 获取原始结果
        content = self.client.basicGeneral(image_file)
        # 获取文字结果
        result = "\n".join([i['words'] for i in content['words_result']])
        return result

ocr_cli = BaiduOcr()

class Application(Frame):
    """百度ocr图像识别程序"""
    def __init__(self, master, **kw):
        """初始化"""
        super().__init__(master, **kw)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        """创建"""
        # 创建文件选择按钮
        self.choose_file_btn = Button(self, text='请选择要识别的图片', command=self.choose_file, justify='left')
        self.choose_file_btn.pack()
        # 创建确定按钮
        self.confirm_btn = Button(self, text='点击此处开始识别', justify='left', command=self.execute_ocr)
        self.confirm_btn.pack()
        # 创建显示框
        self.label1 = Label(self.master, text='识别结果', justify='left')
        self.label1.pack()
        self.result_text = Text(self.master)
        self.result_text.pack()

    def choose_file(self):
        """选择文件"""
        self.filename = askopenfilename(title='选择文件')
        self.result_text.delete('1.0', END)    # 清空text文字内容

    def execute_ocr(self):
        '''执行识别'''
        result = ocr_cli.return_result(self.filename)
        if result:
            self.result_text.insert(1.0, result)
        else:
            showinfo('提示','图片是否有文字？')


if __name__ == '__main__':
    root = Tk()
    root.geometry('400x400+200+300')
    root.title('OCR文字识别')
    app = Application(master=root)
    root.mainloop()
