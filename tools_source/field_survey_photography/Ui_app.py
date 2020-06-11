# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(692, 166)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(130, 40, 431, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_select_path = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_select_path.setObjectName("pushButton_select_path")
        self.horizontalLayout.addWidget(self.pushButton_select_path)
        self.pushButton_run = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_run.setObjectName("pushButton_run")
        self.horizontalLayout.addWidget(self.pushButton_run)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "外业调查拍照图片分类保存"))
        self.pushButton_select_path.setText(_translate("MainWindow", "选择文件夹"))
        self.pushButton_run.setText(_translate("MainWindow", "进行图片分类"))


    @pyqtSlot()
    def on_pushButton_select_path_clicked(self):
        """
        点击选择文件夹按钮
        """
        print("点击选择文件夹")
    
    @pyqtSlot()
    def on_pushButton_run_clicked(self):
        """
        点击进行图片分类按钮
        """
        print("点击选择文件夹")

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
