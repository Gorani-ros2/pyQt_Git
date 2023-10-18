import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtCore import *


from_class = uic.loadUiType("Painter.ui")[0]

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(" Test Painter ")
        
        self.pixmap = QPixmap(self.label.width(), self.label.height())
        self.pixmap.fill(Qt.white)
        self.label.setPixmap(self.pixmap)
        
        self.draw()
        
        self.x, self.y = None, None
    
    def mouseMoveEvent(self, event):    # 누른 상태일 때 이벤트를 받음
        if self.x is None:
            self.x = event.x()
            self.y = event.y()
            return
        
        painter = QPainter(self.label.pixmap())
        painter.drawLine(self.x, self.y, event.x(), event.y())
        painter.end()
        self.update()
        
        self.x = event.x()
        self.y = event.y()
    
    def mouseReleaseEvent(self, event):     # 마우스를 떼면 초기화
        self.x = None
        self.y = None
        
        
        
        
    def draw(self):                             # 선을 긋는 방법과 스타일을 바꾸는 3가지

        
        painter = QPainter(self.label.pixmap())
        self.pen = QPen(Qt.red, 5, Qt.SolidLine)        ### 스타일바꾸기 1 : 이거 밑으로 바뀜. 맨위는 안됨. 페인터가 시작된 후부터 가능
        painter.setPen(self.pen)
        painter.drawLine(100, 100, 500, 100)    # 1. QPainter 사용
        
        
        self.pen.setBrush(Qt.blue)                      ### 스타일바꾸기 2
        self.pen.setWidth(10)
        self.pen.setStyle(Qt.DashDotLine)
        painter.setPen(self.pen)
        self.line = QLine(100, 200, 500, 200)
        painter.drawLine(self.line)             # 2. QLine 사용
        
        
        painter.setPen(QPen(Qt.black, 20, Qt.DotLine))  ### 스타일바꾸기 3
        self.p1 = QPoint(100, 300)
        self.p2 = QPoint(500, 300)
        painter.drawLine(self.p1, self.p2)      # 3. QPoint 사용
        

        # 동그라미 그리기
        painter.setPen(QPen(Qt.red, 5, Qt.SolidLine))
        painter.drawEllipse(50,50, 50,50)   # 동그라미
        
        # 네모그려서 검정색으로 채우기
        painter.setPen(QPen(Qt.green, 5, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.black))  # 이거 밑으로는 다 채워짐
        painter.drawRect(100, 100, 100, 100)    #네모
        
 
        # text 넣기
        self.font = QFont()         #setPen으로 따로 설정해주지 않아 위에 네모의 선 설정을 그대로 가져오게 된다.
        self.font.setFamily('Times')
        self.font.setBold(True)
        self.font.setPointSize(20)
        painter.setFont(self.font)
        painter.drawText(1,20,'This is drawText.')
        
        painter.end

if __name__ == "__main__": 
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec_())