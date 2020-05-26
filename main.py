import sys
import math
import mainWindow, climateZone, afterOK, analog, countingMethod, mathOperations, technology
from PyQt5 import QtWidgets, uic, QtCore, QtGui

#Для конвертирования .ui -> .py
#	pyuic5 name.ui -o name.py

class technologyForm(QtWidgets.QMainWindow):

	def __init__(self, signal1):
		super(technologyForm, self).__init__()
		self.ui = technology.Ui_Dialog()
		self.ui.setupUi(self)
		self.signal = signal1
		self.ui.checkBox.clicked.connect(self.FirstCheck)
		self.ui.checkBox_2.clicked.connect(self.SecondCheck)

		self.ui.radioButton.clicked.connect(self.RadioCheck)
		self.ui.radioButton_2.clicked.connect(self.RadioCheck)
		self.ui.radioButton_3.clicked.connect(self.RadioCheck)
		self.ui.pushButton_2.clicked.connect(self.close)
		self.ui.pushButton.clicked.connect(self.ClickOk)
		self.ui.lineEdit.textEdited.connect(self.ChangetTextKoef1)
		self.ui.lineEdit_2.textEdited.connect(self.ChangeTextKoef2)

		self.FirstKoef = 0
		self.SecondKoef = 0
		self.TherdKoef = 0


	def ChangetTextKoef1(self):
		try:
			self.FirstKoef = float(self.sender().text())
		except:
			pass


	def ChangeTextKoef2(self):
		try:
			self.SecondKoef = float(self.sender().text())
		except:
			pass


	def FirstCheck(self, state):
		if not state:
			self.FirstKoef = 0
			return
		self.ui.lineEdit.setEnabled(state)
		try:
			self.FirstKoef = float(self.ui.lineEdit.text())
		except:
			pass


	def SecondCheck(self, state):
		if not state:
			self.SecondKoef = 0
			return
		self.ui.lineEdit_2.setEnabled(state)
		try:
			self.SecondKoef = float(self.ui.lineEdit_2.text())
		except:
			pass


	def RadioCheck(self, state):
		if state:
			self.TherdKoef = float(self.sender().text())


	def ClickOk(self):
		self.signal.my_signal.emit(5, self.FirstKoef)
		self.signal.my_signal.emit(6, self.SecondKoef)
		self.signal.my_signal.emit(7, self.TherdKoef)
		self.close()


class mathOperationsForm(QtWidgets.QMainWindow):

	def __init__(self, currentIndex, signal2):
		super(mathOperationsForm, self).__init__()
		self.curentIndex = currentIndex
		self.ui = mathOperations.Ui_Dialog()
		self.ui.setupUi(self)
		self.sig = signal2

		self.ui.tabWidget.setCurrentIndex(self.curentIndex)

		self.ui.countInterpol.clicked.connect(self.Interpolation)
		self.ui.countExtrapol.clicked.connect(self.Extrapolation)
		self.ui.lineEdit_5.setText(str(SaveValues.p))


	def Interpolation(self):
		try:
			t1 = float(self.ui.lineEdit.text())
			t2 = float(self.ui.lineEdit_2.text())
			s = float(SaveValues.p)
			s1 = float(self.ui.lineEdit_3.text())
			s2 = float(self.ui.lineEdit_4.text())
			t = float( t1 + ( ((t2 - t1) / (s2 - s1)) * (s - s1)) )
			self.sig.my_signal.emit(8, t)
			self.ui.lineEdit_6.setText(str(t))
		except Exception as e:
			print(str(e))

	def Extrapolation(self):
		try:
			t_min = float(self.ui.lineEdit_7.text())
			s_min = float(self.ui.lineEdit_8.text())
			se = float(self.ui.lineEdit_10.text())
			alpha = float(self.ui.lineEdit_11.text())
			t = float( t_min * ( (se / s_min) ** alpha ) )
			self.ui.lineEdit_12.setText(str("%.5f" % t))
			self.sig.my_signal.emit(9, t)
		except Exception as e:
			print(str(e))

class countingMethodForm(QtWidgets.QMainWindow):

	def __init__(self, signal1):
		super(countingMethodForm, self).__init__()
		self.ui = countingMethod.Ui_Dialog()
		self.ui.setupUi(self)
		self.ui.pushButton_2.clicked.connect(self.close)
		self.ui.pushButton.clicked.connect(self.Count)
		self.ui.comboBox.currentIndexChanged.connect(self.cb_changed)
		self.sig = signal1

	def cb_changed(self, index):
		if index==0:
			self.ui.lineEdit_2.setText("")
			self.ui.lineEdit_3.setText("")
		if index==1:
			self.ui.lineEdit_2.setText("Электроэнергетика")
			self.ui.lineEdit_3.setText("Электроподстанции")


	def Count(self):
		a1 = 11.6
		a2 = 0.2

		c = float(self.ui.lineEdit_4.text())
		if c < 0.1 or c > 1.3:
			self.ui.lineEdit_4.setText("")
			QtWidgets.QMessageBox.about(self, "Ошибка", "Неверное число: допустимый интервал от 0.1 до 1.3")
			
		tn = float((a1 * math.sqrt(c)) + (a2 * c)) 
		self.ui.lineEdit.setText(str("%.5f" % tn))
		self.sig.my_signal.emit(10, tn)


class analogForm(QtWidgets.QMainWindow):

	def __init__(self):
		super(analogForm, self).__init__()
		self.ui = analog.Ui_Dialog()
		self.ui.setupUi(self)

		self.ui.textEdit.setText("")
		self.koeffsignal = MyWidget()
		self.koeffsignal.my_signal.connect(self.RequesKoef)
		self.ui.har_1.clicked.connect(self.HarChecked)
		self.ui.har_2.clicked.connect(self.HarChecked)
		self.ui.har_3.clicked.connect(self.HarChecked)
		self.ui.har_4.clicked.connect(self.HarChecked)
		
		#Эти тоже надо обработать ток хз куда сохранять и пригодится ли это вообще
		#self.ui.pl_1.clicked.connect()
		#self.ui.pl_2.clicked.connect()
		#self.ui.pl_3.clicked.connect()
		
		self.ui.pushButton_3.clicked.connect(self.OpenMathFormInterpol)
		self.ui.pushButton_4.clicked.connect(self.OpenMathFormExtrapol)
		self.ui.pushButton_5.clicked.connect(self.OpenCountingMethodForm)

		self.ui.pushButton_2.clicked.connect(app.exit)
		


	def RequesKoef(self, val, rez):
		if val==8:
			self.ui.lineEdit_2.setText(str(rez))
		if val==9:
			self.ui.lineEdit_3.setText(str(rez))
		if val==10:
			self.ui.lineEdit_4.setText(str(rez))

	def HarChecked(self):
		self.ui.textEdit.setText("")
		if self.ui.har_1.checkState():
			self.ui.textEdit.append(self.ui.har_1.text())

		if self.ui.har_2.checkState():
			self.ui.textEdit.append(self.ui.har_2.text())

		if self.ui.har_3.checkState():
			self.ui.textEdit.append(self.ui.har_3.text())

		if self.ui.har_4.checkState():
			self.ui.textEdit.append(self.ui.har_4.text())


	def OpenMathFormInterpol(self):
		self.mathF = mathOperationsForm(0, self.koeffsignal)
		self.mathF.show()


	def OpenMathFormExtrapol(self):
		self.mathF = mathOperationsForm(1, self.koeffsignal)
		self.mathF.show()


	def OpenCountingMethodForm(self):
		self.cmf = countingMethodForm(self.koeffsignal)
		self.cmf.show()



class SaveValues(object):
	p = 0
	intepolyatsya = 0


class ChangeSqare(object):
	def __init__(self):
		self.__square = 0


	 
	@property
	def square(self):				# Чтение
		return self.__square

	@square.setter
	def Setsquare(self, value):		# Запись
		self.__square = value

	@square.deleter
	def Delsquare(self):			# Удаление
		del self.__square



class afterOkForm(QtWidgets.QMainWindow):

	def __init__(self, name, place):
		super(afterOkForm, self).__init__()
		self.ui = afterOK.Ui_Dialog()
		self.ui.setupUi(self)
		self.ui.lineEdit.setText(name)	
		self.ui.lineEdit_3.setText(place)
		self.ui.pushButton_5.clicked.connect(self.close)
		self.ui.lineEdit_2.textEdited.connect(self.EditS)
		self.change = ChangeSqare()
		self.ui.pushButton_3.clicked.connect(app.exit)
		self.ui.pushButton_4.clicked.connect(self.openAnalogForm)


	def EditS(self):
		try:
			SaveValues.p = float(self.sender().text())
			 
		except Exception as e:
			print(str(e))
	

	def openAnalogForm(self):
		self.af = analogForm()
		self.af.show()	



class climateZoneForm(QtWidgets.QMainWindow):	

	def __init__(self, signal1):
		super(climateZoneForm, self).__init__()
		self.ui = climateZone.Ui_Dialog()
		self.ui.setupUi(self)
		self.signal = signal1
		self.listKoef = {}
		self.KoefSejsm = 0
		
		self.ui.radioButton_4.toggled.connect(self.ChangeLongBuilding)
		self.ui.radioButton_5.toggled.connect(self.ChangeLongBuilding)
		self.ui.radioButton_6.toggled.connect(self.ChangeLongBuilding)

		self.ui.checkBox.clicked.connect(self.ChangeKoef1)
		self.ui.checkBox_2.clicked.connect(self.ChangeKoef2)
		self.ui.lineEdit_4.textEdited.connect(self.ChangeKoef1)
		self.ui.lineEdit_2.textEdited.connect(self.ChangeKoef2)
		self.ui.checkBox_3.clicked.connect(self.ChangeKoefSejsm)
		self.ui.pushButton.clicked.connect(self.ClickOk)

		self.ui.radioButton.toggled.connect(self.ChangeKoefSejsmValue)
		self.ui.radioButton_2.toggled.connect(self.ChangeKoefSejsmValue)
		self.ui.radioButton_3.toggled.connect(self.ChangeKoefSejsmValue)
		self.ui.pushButton_2.clicked.connect(self.close)


	def ClickOk(self):
		try:
			self.signal.my_signal.emit(3, float(self.ui.lineEdit_3.text()))
			self.signal.my_signal.emit(4, float(self.KoefSejsm))
			self.close()
		except:
			pass
		

	def ChangeKoefSejsm(self, statCheck):
		self.ui.label_13.setEnabled(statCheck)
		self.ui.label_14.setEnabled(statCheck)
		self.ui.label_15.setEnabled(statCheck)

		self.ui.radioButton.setEnabled(statCheck)
		self.ui.radioButton_2.setEnabled(statCheck)
		self.ui.radioButton_3.setEnabled(statCheck)


	def ChangeKoefSejsmValue(self, statCheck):
		if statCheck:
			self.KoefSejsm = self.sender().text()


	def ChangeKoef1(self, statCheck):
		if self.ui.checkBox.checkState():
			try:
				self.CheckValues()
				self.ui.lineEdit_3.setText(str(max(self.listKoef.values())))
			except Exception as e:
				print(str(e))
				self.ui.lineEdit_4.setText("")


	def ChangeKoef2(self, statCheck):
		if self.ui.checkBox_2.checkState():
			try:
				self.CheckValues()
				print(self.listKoef)
				self.ui.lineEdit_3.setText(str(max(self.listKoef.values())))
			except:
				self.ui.lineEdit_2.setText("")


	def ChangeLongBuilding(self, k):
		if k:
			radiobutton = self.sender()
			try:
				self.ui.lineEdit.setText(radiobutton.text())
				self.listKoef["koef1"] = float(self.ui.lineEdit_4.text())
				self.listKoef["koef2"] = float(self.ui.lineEdit_2.text())
				self.listKoef["koef3"] = float(radiobutton.text())
				print(self.listKoef)
				self.ui.lineEdit_3.setText(str(max(self.listKoef.values())))
			except:
				self.ui.lineEdit_3.setText("")

	def CheckValues(self):
		try:
			self.listKoef["koef1"] = float(self.ui.lineEdit_4.text())
			self.listKoef["koef2"] = float(self.ui.lineEdit_2.text())
			self.listKoef["koef3"] = float(self.ui.lineEdit.text())
		except Exception as e:
			print(str(e))



class MyWidget(QtWidgets.QWidget):
    my_signal = QtCore.pyqtSignal(int, float)
 
    def __init__(self):
        super(MyWidget, self).__init__()
        
 
        # Обработчик сигнала
        #self.my_signal.connect(self.mySignalHandler)
 
     

class mainForm(QtWidgets.QMainWindow):
	
	def __init__(self):
		super(mainForm, self).__init__()
		self.ui = mainWindow.Ui_Dialog()
		self.ui.setupUi(self)
		self.ui.pushButton.clicked.connect(self.btnClicked)
		 
		self.koeffsignal = MyWidget()
		 
		#self.ui.lineEdit_4.setText(str(8))
		#self.ui.lineEdit_5.setText(str(5))		
		self.koeffsignal.my_signal.connect(self.RequesKoef)
		self.ui.pushButton_2.clicked.connect(self.btnClicked2)
		self.ui.pushButton_3.clicked.connect(self.btnClickOk)
		    
	def btnClicked(self):	
		self.climateZone = climateZoneForm(self.koeffsignal)
		self.climateZone.show()

	def btnClicked2(self):	
		self.teh = technologyForm(self.koeffsignal)
		self.teh.show()		

	def btnClickOk(self):	
		self.name1 = self.ui.lineEdit.text()
		self.place = self.ui.lineEdit_2.text()
		self.afterok = afterOkForm(self.name1, self.place)
		self.afterok.show()


	def RequesKoef(self, val, rez):
		if val==3:
			self.ui.lineEdit_4.setText(str(rez))
		if val==4:
			self.ui.lineEdit_5.setText(str(rez))
		if val==5:
			print(rez)
			self.ui.lineEdit_6.setText(str(rez))
		if val==6:
			print(rez)
			self.ui.lineEdit_8.setText(str(rez))
		if val==7:
			print(rez)
			self.ui.lineEdit_7.setText(str(rez))
  


app = QtWidgets.QApplication([])
root = mainForm()
root.show()

sys.exit(app.exec())