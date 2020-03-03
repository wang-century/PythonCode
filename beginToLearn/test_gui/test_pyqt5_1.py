import sys
from PyQt5.QtWidgets import QApplication, QWidget,QToolTip,QPushButton,QMessageBox
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import QCoreApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()   # 界面绘制交给InitUi方法

    def initUI(self):
        """界面绘制"""
        QToolTip.setFont(QFont('SansSerif',10)) # 设置显示字体（10px滑体字体）
        self.setToolTip('这是一个<b>QWidget</b>窗口') # 创建提示
        btn = QPushButton('按钮1',self)    # 创建按钮
        btn.setToolTip('这是一个<b>QWidget</b>窗口')
        btn.resize(btn.sizeHint())  # 显示默认尺寸
        # 创建退出按钮
        quit_btn = QPushButton('退出',self)
        quit_btn.clicked.connect(QCoreApplication.instance().quit)
        quit_btn.resize(btn.sizeHint())
        quit_btn.move(0,30)


        self.setGeometry(300,300,300,300)   # 设置窗口位置和大小
        self.setWindowTitle('小示例')  # 设置窗口标题
        self.setWindowIcon(QIcon('img/icon.jpg'))
        self.show() # 显示窗口

    def close_tip(self,event):
        """关闭提示"""
        message = QMessageBox.question(self,'提示','是否退出？',QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        if message == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


# if __name__=="__main__":
#     import sys
#     app=QtWidgets.QApplication(sys.argv)
#     widget=QtWidgets.QMainWindow()
#     ui=Ui_MainWindow()
#     ui.setupUi(widget)
#     widget.show()
#     sys.exit(app.exec_())