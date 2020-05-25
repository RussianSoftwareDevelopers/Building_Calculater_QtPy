import sys
import mainWindow
import climateZone
from PyQt5 import QtWidgets, uic, QtCore, QtGui, QtWidgets




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


class mainForm(QtWidgets.QMainWindow):
	
	def __init__(self):
		super(mainForm, self).__init__()
		self.ui = mainWindow.Ui_Dialog()
		self.ui.setupUi(self)
		self.ui.pushButton.clicked.connect(self.btnClicked)


	def btnClicked(self):
		self.climateZone = climateZoneForm()
		self.climateZone.show()
		print("click")
		
        


app = QtWidgets.QApplication([])
root = mainForm()
root.show()

sys.exit(app.exec())