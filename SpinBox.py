import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic


from_class = uic.loadUiType("SpinBox.ui")[0]

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(" Test SpinBox ")
        
        min = self.spinBox.minimum()
        max = self.spinBox.maximum()
        step = self.spinBox.singleStep()
        
        self.editMin.setText(str(min))
        self.editMax.setText(str(max))
        self.editStep.setText(str(step))
        
        self.slider.setRange(min,max)
        self.slider.setSingleStep(step)

        self.pushButton.clicked.connect(self.apply)
        self.slider.valueChanged.connect(self.changeSlider)
        self.spinBox.valueChanged.connect(self.changeSpinBox)
        
        self.pixmap = QPixmap()
        self.pixmap.load('./cat.jpeg')
        
        self.pixmap = self.pixmap.scaled(self.label_4.width(), self.label_4.height())  # 사진크기를 사이즈에 맞추기
        self.label_4.setPixmap(self.pixmap)
        # self.label_4.resize(self.pixmap.width(), self.pixmap.height())  사이즈를 사진크기에 맞추기
        
    
    def changeSpinBox(self):
        actual = self.spinBox.value()
        self.slider.setValue(actual)
    
    def changeSlider(self):
        actual = self.slider.value()
        self.labelValue2.setText(str(actual))
        self.spinBox.setValue(actual)
        
        
    def apply(self):
        min = self.editMin.text()
        max = self.editMax.text()
        step = self.editStep.text()
        
        self.spinBox.setRange(int(min),int(max))
        self.spinBox.setSingleStep(int(step))
        
        self.slider.setRange(int(min),int(max))
        self.slider.setSingleStep(int(step))
        
        
        
if __name__ == "__main__": 
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec_())