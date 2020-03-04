# -*- coding: utf-8 -*-
"""
关于页面设计
"""

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(400, 300)
        About.setSizeGripEnabled(True)
        self.verticalLayoutWidget = QtWidgets.QWidget(About)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 70, 371, 61))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayoutWidget = QtWidgets.QWidget(About)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 150, 371, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_visit_website = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_visit_website.setObjectName("pushButton_visit_website")
        self.horizontalLayout.addWidget(self.pushButton_visit_website)
        self.pushButton_visit_github = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_visit_github.setObjectName("pushButton_visit_github")
        self.horizontalLayout.addWidget(self.pushButton_visit_github)

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "关于"))
        self.label.setText(_translate("About", "该软件使用百度提供的ocr文字识别与PyQt5开发。"))
        self.label_2.setText(_translate("About", "作者：centuryw"))
        self.pushButton_visit_website.setText(_translate("About", "访问作者网站"))
        self.pushButton_visit_github.setText(_translate("About", "访问作者GitHub"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    About = QtWidgets.QDialog()
    ui = Ui_About()
    ui.setupUi(About)
    About.show()
    sys.exit(app.exec_())
