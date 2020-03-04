# -*- coding: utf-8 -*-
"""
批量搜索excel中的关键字
"""
from os.path import join
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PyQt5 import QtWidgets
from glob import glob
from xlrd import open_workbook
from Ui_my_excel import Ui_MainWindow
from about import About

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    批量搜索excel中的关键字(事件处理)
    """
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.open_dir = None


    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        选定文件夹按钮
        """
        self.open_dir = QFileDialog.getExistingDirectory(self,'选择文件夹','/')

    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        开始搜索按钮
        """
        result_file_list = set()   # 用于存放搜索结果文件
        if self.open_dir is None:
            QMessageBox.warning(self,'警告','请先选择文件夹！')
            self.open_dir = QFileDialog.getExistingDirectory(self, '选择文件夹', '/')

        # 获取用户输入
        user_input = self.lineEdit.text()
        user_input = user_input.strip()
        key_list = user_input.split(' ')    # 根据用户输入划分关键字(空格符分割)
        if ''in key_list:
            QMessageBox.warning(self,'警告','请输入正确的关键字(若为多个关键字则用空格隔开)！')
        else:
            print(key_list)
            # 获取该目录下所有excel文件
            dir_files = glob(join(self.open_dir,'*.xlsx'))
            for file in dir_files:
                work_book = open_workbook(file)
                for sheet in work_book.sheets():
                    for row in range(sheet.nrows):
                        for col in range(sheet.ncols):
                            data = str(sheet.cell(row,col).value)
                            for key in key_list:
                                if key in data:
                                    print('在文件{}字符串{}中检索到文字：{}'.format(file,data,key))
                                    self.textBrowser.append('在文件{}内容"{}"中检索到关键字：{}'.format(file,data,key))
                                    result_file_list.add(file)  # 将文件加入搜索结果文件集合
            if len(result_file_list) == 0:  # 如果搜索完所有文件没有搜索到关键字则提示
                QMessageBox.information(self, '提示', '在该目录的excel文件中没有找到输入的关键字')



    @pyqtSlot()
    def on_actiondakai_triggered(self):
        """
        打开
        """
        self.open_dir = QFileDialog.getExistingDirectory(self, '选择文件夹', '/')

    @pyqtSlot()
    def on_action_triggered(self):
        """
        关闭
        """
        self.open_dir = None
    
    @pyqtSlot()
    def on_action_2_triggered(self):
        """
        退出
        """
        exit(0)
    
    @pyqtSlot()
    def on_action_3_triggered(self):
        """
        使用说明
        """
        QMessageBox.information(self, '使用说明', '首先点击“选择文件夹”，选择要检索的excel文件的保存目录，然后在下方输入关键字(关键字以空格作为分隔符，可以输入多个关键字)，然后点击开始搜索，搜索结果将在上方文本区域显示。')


    
    @pyqtSlot()
    def on_action_4_triggered(self):
        """
        关于
        """
        about = About()
        about.exec_()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
    

