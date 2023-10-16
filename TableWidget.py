import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5.QtCore import QDate


from_class = uic.loadUiType("TableWidget.ui")[0]

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(" Test Table Widget")
        self.addButton.clicked.connect(self.aadd)
        self.delButton.clicked.connect(self.deel)

        for gender in ['M','F']:
            self.genderBox.addItem(gender)
        
    
    def aadd(self):
        if self.editName.text()=='':
            self.message.setText('이름을 입력하세요')
            self.message.setStyleSheet('Color : red')
        else:
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QTableWidgetItem(self.editName.text()))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(self.genderBox.currentText()))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(self.editBirthday.text()))
            
            self.message.setText('입력 완료')
            self.message.setStyleSheet('Color : green')
            self.editName.clear()
            self.genderBox.setCurrentText('M')
            qdate = QtCore.QDate.fromString('2000-01-01', 'yyyy-MM-dd')
            self.editBirthday.setDate(qdate)

    def deel(self):
        self.tableWidget.removeRow(0)


if __name__ == "__main__": 
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec_())