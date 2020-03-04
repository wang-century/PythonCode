# -*- coding: utf-8 -*-

"""
关于页面事件处理
"""
import webbrowser

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from Ui_about import Ui_About


class About(QDialog, Ui_About):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(About, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_visit_website_clicked(self):
        """
        访问作者网站按钮（点击事件）
        """
        webbrowser.open('http://centurye.com')
    
    @pyqtSlot()
    def on_pushButton_visit_github_clicked(self):
        """
        访问作者Github按钮（点击事件）
        """
        webbrowser.open('https://github.com/wang-century?tab=repositories')
