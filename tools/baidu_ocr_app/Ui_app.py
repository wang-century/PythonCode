# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\16496\Google 云端硬盘\Code\PythonCode\tools\baidu_ocr_app\app.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralWidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 90, 761, 501))
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(500, 0, 295, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_help = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_help.setObjectName("pushButton_help")
        self.horizontalLayout.addWidget(self.pushButton_help)
        self.pushButton_about = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_about.setObjectName("pushButton_about")
        self.horizontalLayout.addWidget(self.pushButton_about)
        self.pushButton_quit = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_quit.setObjectName("pushButton_quit")
        self.horizontalLayout.addWidget(self.pushButton_quit)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 0, 261, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_choose_img = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_choose_img.setObjectName("pushButton_choose_img")
        self.horizontalLayout_2.addWidget(self.pushButton_choose_img)
        self.pushButton_start_ocr = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_start_ocr.setObjectName("pushButton_start_ocr")
        self.horizontalLayout_2.addWidget(self.pushButton_start_ocr)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.pushButton_quit.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "OCR文字识别"))
        self.pushButton_help.setText(_translate("MainWindow", "帮助"))
        self.pushButton_about.setText(_translate("MainWindow", "关于"))
        self.pushButton_quit.setText(_translate("MainWindow", "退出"))
        self.pushButton_choose_img.setText(_translate("MainWindow", "选择图片"))
        self.pushButton_start_ocr.setText(_translate("MainWindow", "开始识别"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
