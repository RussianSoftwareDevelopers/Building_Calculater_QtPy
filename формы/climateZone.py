# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'climateZone.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(681, 588)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 171, 16))
        self.label.setObjectName("label")
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(20, 30, 641, 201))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 639, 199))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 271, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit.setGeometry(QtCore.QRect(280, 10, 41, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.textBrowser = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser.setGeometry(QtCore.QRect(50, 40, 261, 61))
        self.textBrowser.setObjectName("textBrowser")
        self.radioButton_4 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_4.setGeometry(QtCore.QRect(10, 50, 41, 17))
        self.radioButton_4.setObjectName("radioButton_4")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser_2.setGeometry(QtCore.QRect(360, 40, 261, 61))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.radioButton_5 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_5.setGeometry(QtCore.QRect(320, 50, 41, 17))
        self.radioButton_5.setObjectName("radioButton_5")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser_3.setGeometry(QtCore.QRect(50, 130, 261, 61))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.radioButton_6 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_6.setGeometry(QtCore.QRect(10, 140, 41, 17))
        self.radioButton_6.setObjectName("radioButton_6")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 240, 101, 16))
        self.label_3.setObjectName("label_3")
        self.scrollArea_2 = QtWidgets.QScrollArea(Dialog)
        self.scrollArea_2.setGeometry(QtCore.QRect(20, 260, 641, 41))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 639, 39))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_4.setGeometry(QtCore.QRect(30, 10, 321, 16))
        self.label_4.setObjectName("label_4")
        self.checkBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox.setGeometry(QtCore.QRect(10, 10, 21, 17))
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_5.setGeometry(QtCore.QRect(380, 10, 71, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(460, 10, 31, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 310, 161, 16))
        self.label_6.setObjectName("label_6")
        self.scrollArea_3 = QtWidgets.QScrollArea(Dialog)
        self.scrollArea_3.setGeometry(QtCore.QRect(20, 330, 641, 41))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 639, 39))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_7.setGeometry(QtCore.QRect(30, 10, 421, 16))
        self.label_7.setObjectName("label_7")
        self.checkBox_2 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 10, 21, 17))
        self.checkBox_2.setText("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_8.setGeometry(QtCore.QRect(480, 10, 81, 16))
        self.label_8.setObjectName("label_8")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(560, 10, 31, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(20, 380, 401, 16))
        self.label_9.setObjectName("label_9")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(440, 380, 41, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(490, 550, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(590, 550, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.scrollArea_4 = QtWidgets.QScrollArea(Dialog)
        self.scrollArea_4.setGeometry(QtCore.QRect(20, 420, 641, 121))
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 639, 119))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.label_11.setGeometry(QtCore.QRect(10, 0, 81, 16))
        self.label_11.setObjectName("label_11")
        self.checkBox_3 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_4)
        self.checkBox_3.setGeometry(QtCore.QRect(20, 20, 21, 17))
        self.checkBox_3.setText("")
        self.checkBox_3.setObjectName("checkBox_3")
        self.label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.label_12.setGeometry(QtCore.QRect(40, 20, 201, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.label_13.setEnabled(False)
        self.label_13.setGeometry(QtCore.QRect(40, 50, 261, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.label_14.setEnabled(False)
        self.label_14.setGeometry(QtCore.QRect(40, 70, 541, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.label_15.setEnabled(False)
        self.label_15.setGeometry(QtCore.QRect(40, 90, 111, 16))
        self.label_15.setObjectName("label_15")
        self.radioButton = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_4)
        self.radioButton.setEnabled(False)
        self.radioButton.setGeometry(QtCore.QRect(20, 50, 21, 17))
        self.radioButton.setText("")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_4)
        self.radioButton_2.setEnabled(False)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 70, 21, 17))
        self.radioButton_2.setText("")
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_4)
        self.radioButton_3.setEnabled(False)
        self.radioButton_3.setGeometry(QtCore.QRect(20, 90, 21, 17))
        self.radioButton_3.setText("")
        self.radioButton_3.setObjectName("radioButton_3")
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(20, 400, 71, 16))
        self.label_10.setObjectName("label_10")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Природно-климатические условия"))
        self.label.setText(_translate("Dialog", "Природно-климатический район"))
        self.label_2.setText(_translate("Dialog", "Коэффициент к продолжительности строительства "))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:7pt; color:#2d2d2d; background-color:#ffffff;\">Магаданская обл.; побережье и острова Северного Ледовитого океана, Лещуконский, Мезенский, Пинежский районы и Ненецкий автономный округ Архангельской обл.; Камчатская обл.; Таймырский (Долгано-Ненецкий) и Эвенкийский автономные округа Красноярского края; Чукотский автономный округ Магаданской обл.; Сахалинская обл.; Ханты-Мансийский автономный округ (севернее 60-й параллели); Ямало-Ненецкий автономный округ Тюменской обл.; Охотский район Хабаровского края; Якутская АССР (севернее 60-й параллели);</span></p></body></html>"))
        self.radioButton_4.setText(_translate("Dialog", "1.6"))
        self.textBrowser_2.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:7pt; color:#2d2d2d; background-color:#ffffff;\">Мурманская обл., за исключением Мурманска; гг. Дудинка, Игарка, Норильск и Туруханский район Красноярского края; Якутская АССР (южнее 60-й параллели);</span></p></body></html>"))
        self.radioButton_5.setText(_translate("Dialog", "1.4"))
        self.textBrowser_3.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:7pt; color:#2d2d2d; background-color:#ffffff;\">Амурская обл.; Архангельская обл., за исключением Архангельска и Северодвинска; Бурятская АССР, за исключением Улан-Удэ; Карельская АССР, за исключением Петрозаводска; Коми АССР, Мурманск; Иркутская, Новосибирская, Омская, Томская области и Красноярский край севернее Транссибирской железнодорожной магистрали, за исключением городов, расположенных на этой магистрали, а также Братска и Томска; Пермская обл. севернее 60-й параллели; Приморский край, за исключением Владивостока и Находки; Тувинская АССР; Ханты-Мансийский автономный округ (южнее 60-й параллели) Тюменской обл.; Хабаровский край, за исключением Комсомольска-на-Амуре, Советской Гавани и Хабаровска; Читинская обл., за исключением Читы.</span></p></body></html>"))
        self.radioButton_6.setText(_translate("Dialog", "1.2"))
        self.label_3.setText(_translate("Dialog", "Горная местность "))
        self.label_4.setText(_translate("Dialog", "горная местнотсь с высотой над уровнем моря 1500 м и более "))
        self.label_5.setText(_translate("Dialog", "Коэффициент "))
        self.lineEdit_4.setText(_translate("Dialog", "1.3"))
        self.label_6.setText(_translate("Dialog", "Район пустынь и полупустынь"))
        self.label_7.setText(_translate("Dialog", "средняя температура июля выше 27 С и количество осадков менее 300 мм в год"))
        self.label_8.setText(_translate("Dialog", "Коэффициент"))
        self.lineEdit_2.setText(_translate("Dialog", "1.1"))
        self.label_9.setText(_translate("Dialog", "Итоговый коэффициент по природно-климатическим условиям строительства "))
        self.pushButton.setText(_translate("Dialog", "ОК"))
        self.pushButton_2.setText(_translate("Dialog", "Отмена"))
        self.label_11.setText(_translate("Dialog", "Коэффициент: "))
        self.label_12.setText(_translate("Dialog", "район сейсмичностью 7 баллов и выше"))
        self.label_13.setText(_translate("Dialog", "1.1 - объекты жилищно-гражданского назначения "))
        self.label_14.setText(_translate("Dialog", "1.05 - объекты производственного назанчения, кроме линейных, электроснабжения, транспорта и связи "))
        self.label_15.setText(_translate("Dialog", "1.0 - другие объекты "))
        self.label_10.setText(_translate("Dialog", "Сейсмичность "))
