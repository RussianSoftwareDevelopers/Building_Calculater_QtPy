# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'countingMethod.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(568, 482)
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(10, 80, 551, 41))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 549, 39))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 10, 251, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 71, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(480, 450, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(220, 0, 111, 21))
        self.label.setObjectName("label")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(10, 140, 231, 16))
        self.label_9.setObjectName("label_9")
        self.scrollArea_6 = QtWidgets.QScrollArea(Dialog)
        self.scrollArea_6.setGeometry(QtCore.QRect(10, 160, 551, 41))
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollArea_6.setObjectName("scrollArea_6")
        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 549, 39))
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_6)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 10, 251, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 230, 421, 16))
        self.label_5.setObjectName("label_5")
        self.scrollArea_2 = QtWidgets.QScrollArea(Dialog)
        self.scrollArea_2.setGeometry(QtCore.QRect(10, 260, 551, 91))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 549, 89))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents_2)
        self.scrollArea_3.setGeometry(QtCore.QRect(10, 30, 201, 41))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 199, 39))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_7.setGeometry(QtCore.QRect(10, 0, 181, 41))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("../../GitHub/Building_Calculater_QtPy/countingMethod.PNG"))
        self.label_7.setObjectName("label_7")
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 47, 13))
        self.label_6.setObjectName("label_6")
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_10.setGeometry(QtCore.QRect(220, 10, 141, 16))
        self.label_10.setObjectName("label_10")
        self.label_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_13.setGeometry(QtCore.QRect(370, 10, 171, 20))
        self.label_13.setObjectName("label_13")
        self.scrollArea_13 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents_2)
        self.scrollArea_13.setGeometry(QtCore.QRect(220, 30, 141, 41))
        self.scrollArea_13.setWidgetResizable(True)
        self.scrollArea_13.setObjectName("scrollArea_13")
        self.scrollAreaWidgetContents_17 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_17.setGeometry(QtCore.QRect(0, 0, 139, 39))
        self.scrollAreaWidgetContents_17.setObjectName("scrollAreaWidgetContents_17")
        self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents_17)
        self.label_11.setGeometry(QtCore.QRect(10, 10, 21, 21))
        self.label_11.setObjectName("label_11")
        self.scrollArea_8 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents_17)
        self.scrollArea_8.setGeometry(QtCore.QRect(31, 11, 31, 21))
        self.scrollArea_8.setWidgetResizable(True)
        self.scrollArea_8.setObjectName("scrollArea_8")
        self.scrollAreaWidgetContents_8 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_8.setGeometry(QtCore.QRect(0, 0, 29, 19))
        self.scrollAreaWidgetContents_8.setObjectName("scrollAreaWidgetContents_8")
        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_8)
        self.label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents_17)
        self.label_12.setGeometry(QtCore.QRect(80, 10, 21, 21))
        self.label_12.setObjectName("label_12")
        self.scrollArea_7 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents_17)
        self.scrollArea_7.setGeometry(QtCore.QRect(100, 10, 31, 21))
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollArea_7.setObjectName("scrollArea_7")
        self.scrollAreaWidgetContents_7 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_7.setGeometry(QtCore.QRect(0, 0, 29, 19))
        self.scrollAreaWidgetContents_7.setObjectName("scrollAreaWidgetContents_7")
        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_7)
        self.scrollArea_13.setWidget(self.scrollAreaWidgetContents_17)
        self.scrollArea_14 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents_2)
        self.scrollArea_14.setGeometry(QtCore.QRect(370, 30, 161, 41))
        self.scrollArea_14.setWidgetResizable(True)
        self.scrollArea_14.setObjectName("scrollArea_14")
        self.scrollAreaWidgetContents_18 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_18.setGeometry(QtCore.QRect(0, 0, 159, 39))
        self.scrollAreaWidgetContents_18.setObjectName("scrollAreaWidgetContents_18")
        self.label_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents_18)
        self.label_14.setGeometry(QtCore.QRect(10, 10, 21, 16))
        self.label_14.setObjectName("label_14")
        self.scrollArea_12 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents_18)
        self.scrollArea_12.setGeometry(QtCore.QRect(120, 10, 31, 21))
        self.scrollArea_12.setWidgetResizable(True)
        self.scrollArea_12.setObjectName("scrollArea_12")
        self.scrollAreaWidgetContents_16 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_16.setGeometry(QtCore.QRect(0, 0, 29, 19))
        self.scrollAreaWidgetContents_16.setObjectName("scrollAreaWidgetContents_16")
        self.scrollArea_12.setWidget(self.scrollAreaWidgetContents_16)
        self.label_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents_18)
        self.label_15.setGeometry(QtCore.QRect(90, 10, 41, 21))
        self.label_15.setObjectName("label_15")
        self.scrollArea_11 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents_18)
        self.scrollArea_11.setGeometry(QtCore.QRect(40, 10, 31, 21))
        self.scrollArea_11.setWidgetResizable(True)
        self.scrollArea_11.setObjectName("scrollArea_11")
        self.scrollAreaWidgetContents_15 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_15.setGeometry(QtCore.QRect(0, 0, 29, 19))
        self.scrollAreaWidgetContents_15.setObjectName("scrollAreaWidgetContents_15")
        self.scrollArea_11.setWidget(self.scrollAreaWidgetContents_15)
        self.scrollArea_14.setWidget(self.scrollAreaWidgetContents_18)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 420, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(10, 30, 261, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(300, 30, 261, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(120, 420, 47, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(160, 420, 81, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(10, 390, 47, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(40, 390, 81, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 370, 221, 16))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        self.comboBox.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Расчетный метод"))
        self.label_2.setText(_translate("Dialog", "Отрасль"))
        self.pushButton_2.setText(_translate("Dialog", "Выход"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Расчетный метод</span></p></body></html>"))
        self.label_9.setText(_translate("Dialog", "Подотрасль, вид производтсва или объекта"))
        self.label_5.setText(_translate("Dialog", "Данные для расчетного метоа определения продолжительности строительства"))
        self.label_6.setText(_translate("Dialog", "Формула"))
        self.label_10.setText(_translate("Dialog", "Значение коэффициентов"))
        self.label_13.setText(_translate("Dialog", "Интервал объемов СМР, млн. руб"))
        self.label_11.setText(_translate("Dialog", "А1"))
        self.label_12.setText(_translate("Dialog", "А2"))
        self.label_14.setText(_translate("Dialog", "мин."))
        self.label_15.setText(_translate("Dialog", "макс."))
        self.pushButton.setText(_translate("Dialog", "Расчет"))
        self.comboBox.setCurrentText(_translate("Dialog", "Электроэнергетика"))
        self.comboBox.setItemText(0, _translate("Dialog", "Электроэнергетика"))
        self.comboBox.setItemText(1, _translate("Dialog", "электроподстанции"))
        self.comboBox_2.setCurrentText(_translate("Dialog", "Нефтедобывающая промышленность "))
        self.comboBox_2.setItemText(0, _translate("Dialog", "Нефтедобывающая промышленность "))
        self.label_8.setText(_translate("Dialog", "Тн="))
        self.label_16.setText(_translate("Dialog", "C="))
        self.label_3.setText(_translate("Dialog", "Объем СМР в ценах 1984г. в млн. рублей"))
