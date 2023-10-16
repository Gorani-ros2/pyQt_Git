import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic


from_class = uic.loadUiType("ComboBox.ui")[0]

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(" Test Text ComboBox ")
        
        self.pushButton.clicked.connect(self.seend)
            
        for year in range(1900,2023+1):
            self.cbYear.addItem(str(year))  # 콤보박스 추가 addItem()
        
        for month in range(1,12+1):
            self.cbMonth.addItem(str(month)) 
            
        for day in range(1, 31+1):
            self.cbDay.addItem(str(day))
    
        self.cbYear.setCurrentText(str(1990))  # 콤보박스 텍스트 지정 setCurrentText()
        
        self.calendarWidget.clicked.connect(self.selectDate)
        
    def selectDate(self):
        date = self.calendarWidget.selectedDate()  # 캘린더 선택 selectedDate()
        year = date.toString('yyyy') # 캘린더 텍스트 가져오기 toStirng()
        month = date.toString('M')
        day = date.toString('d')
        
        self.cbYear.setCurrentText(year)  # 콤보박스 텍스트 지정하기 setCurrentText() 
        self.cbMonth.setCurrentText(month)
        self.cbDay.setCurrentText(day)
        self.lineEdit.setText(year+'-'+month.zfill(2)+'-'+day.zfill(2))
    
    def seend(self):
        year = self.cbYear.currentText()  # 콤보박스 텍스트 가져오기 currentText() 
        month = self.cbMonth.currentText()
        day = self.cbDay.currentText()
        self.lineEdit.setText(year+'-'+month.zfill(2)+'-'+day.zfill(2))
        
    
if __name__ == "__main__": 
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec_())