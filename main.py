import sys
import mainWindow, climateZone, afterOK, analog, countingMethod, mathOperations, technology
from PyQt5 import QtWidgets, uic, QtCore, QtGui



class technologyForm(QtWidgets.QMainWindow):

	def __init__(self):
		super(technologyForm, self).__init__()
		self.ui = technology.Ui_Dialog()
		self.ui.setupUi(self)



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



class afterOkForm(QtWidgets.QMainWindow):

	def __init__(self):
		super(afterOkForm, self).__init__()
		self.ui = afterOK.Ui_Dialog()
		self.ui.setupUi(self)	


class climateZoneForm(QtWidgets.QMainWindow):	

	def __init__(self):
		super(climateZoneForm, self).__init__()
		self.ui = climateZone.Ui_Dialog()
		self.ui.setupUi(self)

		self.listKoef = {}
		
		
		
		self.ui.radioButton_4.toggled.connect(self.ChangeLongBuilding)
		self.ui.radioButton_5.toggled.connect(self.ChangeLongBuilding)
		self.ui.radioButton_6.toggled.connect(self.ChangeLongBuilding)

		self.ui.checkBox.clicked.connect(self.ChangeKoef1)
		self.ui.checkBox_2.clicked.connect(self.ChangeKoef2)
		self.ui.lineEdit_4.textEdited.connect(self.ChangeKoef1)
		self.ui.lineEdit_2.textEdited.connect(self.ChangeKoef2)
		self.ui.checkBox_3.clicked.connect(self.ChangeKoefSejsm)
		self.ui.pushButton.clicked.connect(self.ClickOk)

	def ClickOk(self):
		signal.emit(3, 6.0)


	def ChangeKoefSejsm(self, statCheck):
		self.ui.label_13.setEnabled(statCheck)
		self.ui.label_14.setEnabled(statCheck)
		self.ui.label_15.setEnabled(statCheck)

		self.ui.radioButton.setEnabled(statCheck)
		self.ui.radioButton_2.setEnabled(statCheck)
		self.ui.radioButton_3.setEnabled(statCheck)

		 


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
        self.my_signal.connect(self.mySignalHandler)
 
    def mySignalHandler(self, data):  # Вызывается для обработки сигнала
        print(data)



class mainForm(QtWidgets.QMainWindow):
	
	def __init__(self):
		super(mainForm, self).__init__()
		self.ui = mainWindow.Ui_Dialog()
		self.ui.setupUi(self)
		self.ui.pushButton.clicked.connect(self.btnClicked)
		koeff =  KoefficientSetGet()
		koeffsignal = MyWidget()
		koeff.age = 3
		self.ui.lineEdit_4.setText(str(koeff.age))
		self.ui.lineEdit_5.setText(str(5))		

		

		   #connect(self.koeffsignal)

	def btnClicked(self):	
		self.climateZone = climateZoneForm()
		self.climateZone.show()
		print("click")

	def RequesKoef(self, val):
		print(val)


class KoefficientSetGet(): 
	def __init__(self):
		self._age = 0
		self._age = 0

     # using property decorator 
     # a getter function 
	@property
	def age(self): 
		print("getter method called") 
		return self._age
		   
	@age.setter
	def age(self, a): 
		self._age = a 
  


app = QtWidgets.QApplication([])
root = mainForm()
root.show()


sys.exit(app.exec())