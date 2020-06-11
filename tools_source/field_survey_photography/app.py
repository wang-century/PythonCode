# -*- coding: utf-8 -*-

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QApplication, QMessageBox, QSplashScreen, QAction
from os import system
from Ui_app import Ui_MainWindow
from script import classify_directory

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    事件处理
    """
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_select_path_clicked(self):
        """
        点击选择文件夹按钮
        """
        print("点击选择文件夹")
        self.directory_name = QFileDialog.getExistingDirectory(self, '选择文件夹')  # 获取要打开的文件路径
        self.directory_name = self.directory_name.replace('/','\\')
        print(self.directory_name)

    
    @pyqtSlot()
    def on_pushButton_run_clicked(self):
        """
        点击进行图片分类按钮
        """
        print("点击选择文件夹")
        classify_directory(self.directory_name)
        # system("explorer.exe {}".format(self.directory_name)) 
        

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    # splash = QSplashScreen(QPixmap("start_tip.jpg"))  # 创建启动提示
    # 创建字体
    # font = QFont()
    # font.setPointSize(40)
    # splash.setFont(font)  # 设置启动界面中字体大小
    # splash.show()
    # splash.showMessage('正在启动程序......', Qt.AlignCenter, Qt.white, )
    app.processEvents()  # 防止卡死
    window = MainWindow()
    window.show()
    # splash.finish(window)
    sys.exit(app.exec_())