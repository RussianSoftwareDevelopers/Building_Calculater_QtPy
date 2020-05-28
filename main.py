import sys
import math
import mainWindow, climateZone, afterOK, analog, countingMethod, mathOperations, technology
from PyQt5 import QtWidgets, uic, QtCore, QtGui


def ConverFromComma(val):
	""" 
	Функция обрабатывает ошибки при вводе дробных чиесл: замена запятой на точку 
	"""
	if ',' in val:
		return val.replace(',', '.')
	else:
		return val

class technologyForm(QtWidgets.QMainWindow):
	"""
	Класс отвечает за окно приложения "Технология строительства"
	и за обработку действий пользователя на этом окне
	"""
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
	"""
	Класс отвечает за окно "Вычисления"
	и выполняет подсчет с помощью интерполяции и экстраполяции
	"""

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
		self.ui.lineEdit_5.textChanged.connect(self.changeS)


	def changeS(self):
		try:
			SaveValues.p = float(ConverFromComma(self.sender().text()))

		except:
			pass


	def Interpolation(self):
		""" Функция интерполяции """
		try:
			t1 = float(ConverFromComma(self.ui.lineEdit.text()))
			t2 = float(ConverFromComma(self.ui.lineEdit_2.text()))
			s = float(SaveValues.p)
			s1 = float(ConverFromComma(self.ui.lineEdit_3.text()))
			s2 = float(ConverFromComma(self.ui.lineEdit_4.text()))
			t = float( t1 + ( ((t2 - t1) / (s2 - s1)) * (s - s1)) )
			self.sig.my_signal.emit(8, t)
			self.ui.lineEdit_6.setText(str("%.1f" % t))
		except Exception as e:
			print(str(e))


	def Extrapolation(self):
		""" Функция экстраполяции """
		try:
			t_min = float(ConverFromComma(self.ui.lineEdit_7.text()))
			s_min = float(ConverFromComma(self.ui.lineEdit_8.text()))
			se = float(ConverFromComma(self.ui.lineEdit_10.text()))
			alpha = float(ConverFromComma(self.ui.lineEdit_11.text()))
			t = float( t_min * ( (se / s_min) ** alpha ) )
			self.ui.lineEdit_12.setText(str("%.2f" % t))
			self.sig.my_signal.emit(9, t)
		except Exception as e:
			print(str(e))



class countingMethodForm(QtWidgets.QMainWindow):
	"""
	Класс отвечает за окно "Рвсчетный метод"
	и выполняет соответствующие вычисления
	"""
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
			self.ui.label_4.setText(" 11.6")
			self.ui.label_17.setText(" 0.2")
			self.ui.label_18.setText(" 0.1")
			self.ui.label_19.setText(" 1.3")


	def Count(self):
		""" Функция расчетного метода """
		a1 = 11.6
		a2 = 0.2

		try:
			c = float(ConverFromComma(self.ui.lineEdit_4.text()))
			if c < 0.1 or c > 1.3:
				self.ui.lineEdit_4.setText("")
				QtWidgets.QMessageBox.about(self, "Ошибка", "Неверное число: допустимый интервал от 0.1 до 1.3")
				return
			
			tn = float((a1 * math.sqrt(c)) + (a2 * c)) 
			self.ui.lineEdit.setText(str("%.2f" % tn))
			self.sig.my_signal.emit(10, tn)
		except Exception as e:
			print(str(e))



class analogForm(QtWidgets.QMainWindow):
	"""
	Класс отвечает за окно "Выбор объекта аналога"
	из него осуществляется переход к окнам для вычисления продолжительности строительства
	"""
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
			
		self.ui.pushButton.clicked.connect(self.CountBuildingLong)
		self.ui.pushButton_3.clicked.connect(self.OpenMathFormInterpol)
		self.ui.pushButton_4.clicked.connect(self.OpenMathFormExtrapol)
		self.ui.pushButton_5.clicked.connect(self.OpenCountingMethodForm)

		self.ui.pl_1.toggled.connect(self.radioChenge)
		self.ui.pl_2.toggled.connect(self.radioChenge)
		self.ui.pl_3.toggled.connect(self.radioChenge)

		self.ui.pushButton_2.clicked.connect(app.exit)
		self.ui.comboBox.currentIndexChanged.connect(self.cb_changed)

		self.ui.pushButton_6.clicked.connect(self.calculate)

	def calculate(self):
		result = 0
		for k in SaveValues.listkoef:
			if k != 0:
				result = result*k

		




	def cb_changed(self, index):
		self.ui.label_3.setText(self.sender().currentText())
		print(index)


	def RequesKoef(self, val, rez):
		if val==8:
			self.ui.lineEdit_2.setText(str("%.2f" % rez))
		if val==9:
			self.ui.lineEdit_3.setText(str("%.2f" % rez))
		if val==10:
			self.ui.lineEdit_4.setText(str("%.2f" % rez))


	def radioChenge(self):
		if self.ui.har_1.checkState():
			self.CheckRbts()


	def CheckRbts(self):
		if self.ui.pl_1.isChecked():
			self.ui.label_8.setText(" 8,00")
		if self.ui.pl_2.isChecked():
			self.ui.label_8.setText(" 9,00")
		if self.ui.pl_3.isChecked():
			self.ui.label_8.setText(" 9,50")	


	def HarChecked(self):
		self.ui.textEdit.setText("")
		if self.ui.har_1.checkState():
			self.CheckRbts()
			self.ui.textEdit.append(self.ui.har_1.text())
		else:
			self.ui.label_8.setText("")


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


	def CountBuildingLong(self):
		try:
			result = float(ConverFromComma(self.ui.lineEdit_5.text())) / 10
			self.ui.lineEdit_6.setText(str(result))
		except:
			QtWidgets.QMessageBox.about(self, "Ошибка", "Введите число")

class SaveValues(object):
	p = 0
	intepolyatsya = 0

	listkoef = []
	pku = 0
	sejs = 0
	objlitemk = 0
	objblockmet = 0
	smennost = 0



class ChangeSqare(object):
	""" Служебный класс для передачи значений между окнами """
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
	"""
	Класс отвечает за окно "Объект"
	и обрабатывает действия пользоваеля 
	"""
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
	"""
	Класс отвечает за окно "Природно-климатические условия"
	собирает выбранные пользователем коэффициенты 
	и передает их в главное окно
	"""
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
		except Exception as e:
			print(str(e))
		

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
				self.listKoef["koef1"] = float(ConverFromComma(self.ui.lineEdit_4.text()))
				self.ui.lineEdit_3.setText(str(max(self.listKoef.values())))
			except Exception as e:
				print(str(e))
				self.ui.lineEdit_4.setText("")
		else:
			if 'koef1' in self.listKoef.keys():
				del self.listKoef["koef1"]

	def ChangeKoef2(self, statCheck):
		if self.ui.checkBox_2.checkState():
			try:
				self.listKoef["koef2"] = float(ConverFromComma(self.ui.lineEdit_2.text()))
				print(self.listKoef)
				self.ui.lineEdit_3.setText(str(max(self.listKoef.values())))
			except:
				self.ui.lineEdit_2.setText("")
		else:
			if 'koef2' in self.listKoef.keys():
				del self.listKoef["koef2"]



	def ChangeLongBuilding(self, k):
		if k:
			radiobutton = self.sender()
			try:
				self.ui.lineEdit.setText(radiobutton.text())
				if self.ui.checkBox.checkState():
					self.listKoef["koef1"] = float(self.ui.lineEdit_4.text())
				if self.ui.checkBox_2.checkState():
					self.listKoef["koef2"] = float(self.ui.lineEdit_2.text())
				
				self.listKoef["koef3"] = float(radiobutton.text())
				print(self.listKoef)
				self.ui.lineEdit_3.setText(str(max(self.listKoef.values())))
			except:
				self.ui.lineEdit_3.setText("")
				QtWidgets.QMessageBox.about(self, "Ошибка", "Введите значение")



class MyWidget(QtWidgets.QWidget):
    my_signal = QtCore.pyqtSignal(int, float)
 
    def __init__(self):
        super(MyWidget, self).__init__()

     

class mainForm(QtWidgets.QMainWindow):
	""" 
	Основное окно программы
	класс обрабатывает действия пользователя на этом окне
	"""
	def __init__(self):
		super(mainForm, self).__init__()
		self.ui = mainWindow.Ui_Dialog()
		self.ui.setupUi(self)
		self.ui.pushButton.clicked.connect(self.btnClicked)
		 
		self.koeffsignal = MyWidget()
		 		
		self.koeffsignal.my_signal.connect(self.RequesKoef)
		self.ui.pushButton_2.clicked.connect(self.btnClicked2)
		self.ui.pushButton_3.clicked.connect(self.btnClickOk)
		self.ui.pushButton_4.clicked.connect(self.close)
		    

	def btnClicked(self):	
		self.climateZone = climateZoneForm(self.koeffsignal)
		self.climateZone.show()

	def btnClicked2(self):	
		self.teh = technologyForm(self.koeffsignal)
		self.teh.show()		

	def btnClickOk(self):	
		self.name1 = self.ui.lineEdit.text()
		self.place = self.ui.lineEdit_2.text()
		SaveValues.listkoef = [] 

		SaveValues.listkoef.append(self.toFloat(self.ui.lineEdit_4.text()))
		SaveValues.listkoef.append(self.toFloat(self.ui.lineEdit_5.text()))
		SaveValues.listkoef.append(self.toFloat(self.ui.lineEdit_6.text()))
		SaveValues.listkoef.append(self.toFloat(self.ui.lineEdit_8.text()))
		SaveValues.listkoef.append(self.toFloat(self.ui.label_7.text()))

		#SaveValues.pku = self.toFloat(self.ui.lineEdit_4.text())
		#SaveValues.sejs = self.toFloat(self.ui.lineEdit_5.text())
		#SaveValues.objlitemk = self.toFloat(self.ui.lineEdit_6.text())
		#SaveValues.objblockmet = self.toFloat(self.ui.lineEdit_8.text())
		#SaveValues.smennost = self.toFloat(self.ui.label_7.text())

		


		self.afterok = afterOkForm(self.name1, self.place)
		self.afterok.show()


	def toFloat(self, text):
		try:
			return float(ConverFromComma(text))
		except:
			return 0

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