# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mathOperations.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os

class Ui_Dialog(object):
    def resource_path(self, relative):

        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative)
        else:
            return os.path.join(os.path.abspath("."), relative)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(581, 583)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(20, 10, 561, 571))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.image_1 = QtWidgets.QLabel(self.tab)
        self.image_1.setGeometry(QtCore.QRect(30, 0, 501, 211))
        self.image_1.setText("")
        self.image_1.setPixmap(QtGui.QPixmap(self.resource_path("interpolation.PNG")))
        self.image_1.setObjectName("image_1")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(10, 250, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(10, 280, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(10, 310, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(10, 340, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(10, 370, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(50, 250, 61, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 280, 61, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(50, 310, 61, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_4.setGeometry(QtCore.QRect(50, 340, 61, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_5.setGeometry(QtCore.QRect(50, 370, 61, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(140, 370, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_6.setGeometry(QtCore.QRect(180, 370, 61, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.countInterpol = QtWidgets.QPushButton(self.tab)
        self.countInterpol.setGeometry(QtCore.QRect(140, 250, 101, 41))
        self.countInterpol.setObjectName("countInterpol")
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(140, 350, 81, 16))
        self.label_12.setObjectName("label_12")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_7.setGeometry(QtCore.QRect(130, 380, 61, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_8.setGeometry(QtCore.QRect(130, 410, 61, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(10, 410, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(100, 470, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(220, 470, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(90, 440, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_10.setGeometry(QtCore.QRect(130, 440, 61, 20))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_11.setGeometry(QtCore.QRect(130, 470, 61, 20))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_12.setGeometry(QtCore.QRect(260, 470, 61, 20))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(0, 0, 561, 281))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("экстра 111.PNG"))
        self.label_8.setObjectName("label_8")
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setGeometry(QtCore.QRect(10, 380, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.image_2 = QtWidgets.QLabel(self.tab_2)
        self.image_2.setGeometry(QtCore.QRect(0, 0, 561, 361))
        self.image_2.setText("")
        self.image_2.setPixmap(QtGui.QPixmap(self.resource_path("extrapolation.PNG")))
        self.image_2.setObjectName("image_2")
        self.countExtrapol = QtWidgets.QPushButton(self.tab_2)
        self.countExtrapol.setGeometry(QtCore.QRect(220, 380, 81, 41))
        self.countExtrapol.setObjectName("countExtrapol")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(220, 450, 71, 16))
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Вычисления"))
        self.label_2.setText(_translate("Dialog", "T1="))
        self.label_3.setText(_translate("Dialog", "T2="))
        self.label_4.setText(_translate("Dialog", "S1="))
        self.label_5.setText(_translate("Dialog", "S2="))
        self.label_6.setText(_translate("Dialog", "S="))
        self.label_7.setText(_translate("Dialog", "T="))
        self.countInterpol.setText(_translate("Dialog", "Расчитать"))
        self.label_12.setText(_translate("Dialog", "Результат:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Интерполяция "))
        self.label_9.setText(_translate("Dialog", "Sмин(макс)="))
        self.label_10.setText(_translate("Dialog", "α="))
        self.label_11.setText(_translate("Dialog", "Tэ="))
        self.label_13.setText(_translate("Dialog", "Sэ="))
        self.label_14.setText(_translate("Dialog", "Тмин(макс)="))
        self.countExtrapol.setText(_translate("Dialog", "Расчитать"))
        self.label.setText(_translate("Dialog", "Результат:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Экстраполяция "))
