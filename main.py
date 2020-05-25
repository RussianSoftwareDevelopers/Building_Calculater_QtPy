import sys
import mainWindow, climateZone, afterOK, analog, countingMethod, mathOperations, technology
from PyQt5 import QtWidgets, uic, QtCore, QtGui



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

	def __init__(self):
		super(mathOperationsForm, self).__init__()
		self.ui = mathOperations.Ui_Dialog()
		self.ui.setupUi(self)



class countingMethodForm(QtWidgets.QMainWindow):

	def __init__(self):
		super(countingMethodForm, self).__init__()
		self.ui = countingMethod.Ui_Dialog()
		self.ui.setupUi(self)


class analogForm(QtWidgets.QMainWindow):

	def __init__(self):
		super(analogForm, self).__init__()
		self.ui = analog.Ui_Dialog()
		self.ui.setupUi(self)	



class ChangeSqare(object):  
    def __init__(self):
        self.__square = 0
 
    @property
    def square(self):                       # Чтение
        return self.__square
    @square.setter
    def Setsquare(self, value):                # Запись
        self.__square = value
    @square.deleter
    def Delsquare(self):                       # Удаление
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
		self.ui.pushButton_4.clicked.connect()


	def EditS(self):
		try:
			self.change.Setsquare = float(self.sender().text())
		except Exception as e:
			pass
		


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