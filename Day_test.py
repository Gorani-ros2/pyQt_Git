import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic


from_class = uic.loadUiType("Day_test.ui")[0]

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(" Test - DAY ")
        
        self.loadbtn.clicked.connect(self.openFile) 
        self.savebtn.clicked.connect(self.saveFile)
 
        min = self.slider.minimum()
        max = self.slider.maximum()
        step = self.slider.singleStep()

        self.slider.setRange(min,max)
        self.slider.setSingleStep(step)
        self.slider.valueChanged.connect(self.changeSlider)
        # self.pixmap = None
        
    def saveFile(self):
        # sname = QFileDialog.getSaveFileName(self,"Save File", "","")
        # filepath = sname[0]
        # self.pixmap.save(filepath)
        self.pixmap.save('test_cat.jpg')
        
    def changeSlider(self):
        actual = self.slider.value()
        self.label.setFixedHeight(actual)
        self.label.setFixedWidth(actual)
        
        
    def openFile(self):
        name = QFileDialog.getOpenFileName(self, "Choose File", "", " Images(*.jpeg)")
        imagePath = name[0]
        self.pixmap = QPixmap(imagePath)
        self.pixmap = self.pixmap.scaled(self.label.width(), self.label.height())
        self.label.setPixmap(QPixmap(self.pixmap))
        
        
if __name__ == "__main__": 
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec_())