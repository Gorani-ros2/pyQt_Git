import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtGui, uic
from PyQt5.QtCore import *


from_class = uic.loadUiType("PainterMouse.ui")[0]

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(" Test Mouse ")
        self.x, self.y = None, None
        
    
    def mouseMoveEvent(self, event):    # 누른 상태일 때 이벤트를 받음
        # if self.x is None:
        #     self.x = event.x()
        #     self.y = event.y()
        self.x = event.x()
        self.y = event.y()
        self.label_1.setText(f'{self.x}, {self.y}')
            
        self.x = event.globalX()
        self.y = event.globalY()
        

        self.label_2.setText(f'{self.x}, {self.y}')
        

    def mousePressEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            self.label_3.setText('Left')
        elif event.buttons() & Qt.RightButton:
            self.label_3.setText('Right')
        else:
            pass
        
    def wheelEvent(self, event):
        self.label_4.setText(f'{event.angleDelta().x()}, {event.angleDelta().y()}')
        
    
    def mouseReleaseEvent(self, event):     # 마우스를 떼면 초기화
        self.x = None
        self.y = None

if __name__ == "__main__": 
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec_())