import sys
import cv2, imutils
import time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
from datetime import datetime


class Camera(QThread):
    update = pyqtSignal()
    
    def __init__(self, sec=0, parent=None):
        super().__init__()
        self.main = parent
        self.running = True
    
    def run(self):
        while self.running == True:
            self.update.emit()
            time.sleep(0.05)
    
    def stop(self):
        self.running = False    
    

from_class = uic.loadUiType("Opencv.ui")[0]

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(" Connect openCV with pyQt ")
        
        self.isCameraOn = False
        self.isRecStart = False
        self.btnRcord.hide()
        self.btnCapture.hide()
        
        self.pixmap = QPixmap()
        self.camera = Camera(self)
        self.camera.daemon = True
        self.record = Camera(self)
        self.record.daemon = True
        
        self.pushButton.clicked.connect(self.openFile)
        self.pushButton_2.clicked.connect(self.clickCamera)
        self.camera.update.connect(self.updateCamera)
        self.btnRcord.clicked.connect(self.clickRecord)
        self.record.update.connect(self.updateRecording)
        self.btnCapture.clicked.connect(self.capture)
        
        
    def capture(self):
        retval, image = self.video.read()
        if retval :
            self.now = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = self.now+'.png'
            cv2.imwrite(filename, image)
        
        
        
    def updateRecording(self):
        retval, image = self.video.read()
        if retval :
            self.writer.write(image)
        
    
    
    def clickRecord(self):
        if self.isRecStart == False:
            self.btnRcord.setText('Rec Stop')
            self.isRecStart = True
            
            self.recordingStart()
        else:
            self.btnRcord.setText('Rec Start')
            self.isRecStart = False
            
            self.recordingStop()
            
            
            
    def recordingStart(self):
        self.record.running = True
        self.record.start()
        
        self.now = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = self.now + '.avi'
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')
        
        w = int(self.video.get(cv2.CAP_PROP_FRAME_WIDTH))
        h = int(self.video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        self.writer = cv2.VideoWriter(filename, self.fourcc, 20.0, (w, h))
        
        
        
    
    def recordingStop(self):
        self.record.running = False
        
        if self.isRecStart == True:
            self.writer.release()
            
            
        
    def updateCamera(self):
        retval, image = self.video.read()
        if retval :
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
            h,w,c = image.shape
            qiamge = QImage(image.data, w, h, w*c, QImage.Format_RGB888)
            
            self.pixmap = self.pixmap.fromImage(qiamge)
            self.pixmap = self.pixmap.scaled(self.label.width(), self.label.height())
            
            self.label.setPixmap(self.pixmap)
        
        
        
    def clickCamera(self):
        if self.isCameraOn == False:
            self.pushButton_2.setText('Camera OFF')
            self.isCameraOn = True
            self.btnRcord.show()
            self.btnCapture.show()
            
            self.cameraStart()
        else :
            self.pushButton_2.setText('Camera ON')
            self.isCameraOn = False
            self.btnRcord.hide()
            self.btnCapture.hide()
            
            self.cameraStop()
            self.recordingStop()
            
    
    def cameraStart(self):
        self.camera.running = True
        self.camera.start()
        self.video = cv2.VideoCapture(-1)
        
    def cameraStop(self):
        self.camera.running = False
        self.video.release
        
        
    
    def openFile(self):
        file = QFileDialog.getOpenFileName(filter='Image (*.*)')
        
        image = cv2.imread(file[0])
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        h,w,c = image.shape
        qiamge = QImage(image.data, w, h, w*c, QImage.Format_RGB888)
        
        self.pixmap = self.pixmap.fromImage(qiamge)
        self.pixmap = self.pixmap.scaled(self.label.width(), self.label.height())
        
        self.label.setPixmap(self.pixmap)
        

if __name__ == "__main__": 
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec_())