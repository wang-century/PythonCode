# -*- coding: utf-8 -*-
"""
百度ocr文字识别事件处理与运行
@author centuryw
"""
from time import sleep
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QApplication, QMessageBox, QSplashScreen, QAction
from Ui_app import Ui_MainWindow
from baiduOcr import BaiduOcr
from about import About


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    百度ocr文字识别事件处理
    """

    def __init__(self, parent=None):
        """
        初始化，配置图形界面，生成百度ocr工具对象
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.ocr_cli = BaiduOcr()
        self.openfile_name = None  # 初始化打开的图片为空，用于判定是否已经打开图片，防止识别时出现错误

    @pyqtSlot()
    def on_action_help_triggered(self):
        """
        帮助（点击事件）
        """
        QMessageBox.information(self, '帮助', '使用方式：\n点击“选择图片”，选择要识别文字的图片并确定，点击开始识别，识别结果将在下方文本框中显示。\n可以将识别结果复制到要保存的地方。')

    @pyqtSlot()
    def on_action_abou_triggered(self):
        """
        关于（点击事件）
        """
        about = About()
        about.exec_()

    @pyqtSlot()
    def on_action_quit_triggered(self):
        """
        退出（点击事件）
        """
        exit(0)

    @pyqtSlot()
    def on_pushButton_choose_img_clicked(self):
        """
        选择图片按钮（点击事件）
        """
        self.openfile_name = QFileDialog.getOpenFileName(self, '选择文件', '', "All Files(*.jpg , *.png)")[0]  # 获取要打开的文件路径

    @pyqtSlot()
    def on_pushButton_start_ocr_clicked(self):
        """
        开始识别按钮（点击事件）
        """
        if self.openfile_name is not None:
            # 处理获打开文件时获取的文件名
            result = self.ocr_cli.return_result(self.openfile_name)
            self.textEdit.setText(result)
        else:
            QMessageBox.warning(self, '警告', '请先选择要识别的图片！')



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    splash = QSplashScreen(QPixmap("start_tip.jpg"))  # 创建启动提示
    # 创建字体
    font = QFont()
    font.setPointSize(40)
    splash.setFont(font)  # 设置启动界面中字体大小
    splash.show()
    splash.showMessage('正在启动程序......', Qt.AlignCenter, Qt.white, )
    app.processEvents()  # 防止卡死
    window = MainWindow()
    window.show()
    splash.finish(window)
    sys.exit(app.exec_())
