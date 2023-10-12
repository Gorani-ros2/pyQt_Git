import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic


from_class = uic.loadUiType("TextEdit.ui")[0]

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(" Test Text Edit ")
        
        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(lambda: self.setFont("Ubuntu"))  # 람다 학습하기
        self.pushButton_3.clicked.connect(lambda: self.setFont("NanumGothic"))
        
        self.pushButton_4.clicked.connect(lambda: self.setTextColor(255,0,0))
        self.pushButton_5.clicked.connect(lambda: self.setTextColor(0,255,0))
        self.pushButton_6.clicked.connect(lambda: self.setTextColor(0,0,255))
        
        self.pushButton_7.clicked.connect(self.setTextSize)
    
    
    ## 함수를 새로 선언한다고 해서 이름을 아무거나 쓰면 안됨.
    def setTextSize(self):
        size = int(self.lineEdit.text())
        self.textEdit_2.selectAll()
        self.textEdit_2.setFontPointSize(size)
        self.textEdit_2.moveCursor(QTextCursor.End)
    
    
    def add(self):
        txt = self.textEdit.toPlainText()  ## getText() 아님. 그냥 text()
        self.textEdit.clear()
        self.textEdit_2.append(txt)  ## textBrowser.setText.append 아님. setText 안씀.


    def setTextColor(self, r, g, b):  ## 컬러를 바꾸려면 선택해야한다.
        color = QColor(r,g,b)
        self.textEdit_2.selectAll()  ## 전체선택하고
        self.textEdit_2.setTextColor(color)  ## 컬러 입히고
        self.textEdit_2.moveCursor(QTextCursor.End)  ## 선택 초기화
        
        
    def setFont(self, fontName):
        font = QFont(fontName, 15)
        self.textEdit_2.setFont(font)
        


if __name__ == "__main__": 
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec_())