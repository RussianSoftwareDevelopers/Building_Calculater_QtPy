from PyQt5 import QtWidgets, uic
import sys

app = QtWidgets.QApplication([])
win = uic.loadUi("mainWindow.ui")

win.pushButton_4.text = "WWW"

win.show()
sys.exit(app.exec())