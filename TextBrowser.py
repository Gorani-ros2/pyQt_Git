import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic


from_class = uic.loadUiType("TextBrowser.ui")[0]

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(" Test Text Browser ")
        
        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.delete)
        self.lineEdit.returnPressed.connect(self.add)  # 엔터키 활성화
    
    
    def add(self):
        txt = self.lineEdit.text()  ## getText() 아님. 그냥 text()
        self.lineEdit.setText("")   ## setText("")보단 clear()
        self.textBrowser.append(txt)  ## textBrowser.setText.append 아님. setText 안씀.
                                    ## textBrowser는 toPlainText()
    def delete(self):
        self.lineEdit.clear()
        self.textBrowser.clear()

if __name__ == "__main__": 
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec_())