import sys
import cv2
import numpy as np
import time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from datetime import datetime

from_class = uic.loadUiType("oneday_camera.ui")[0]


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
    
    

class VideoThread(QThread):
    frame_loaded = pyqtSignal(QImage)
    
    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path
        self.playing = False
        self.total_frames = 0
        self.current_frame = 0

    def run(self):
        
        self.cap = cv2.VideoCapture(self.file_path)
        fps = self.cap.get(cv2.CAP_PROP_FPS)
        frame_interval = int(np.round((1/fps)*1200))
        self.total_frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        while self.current_frame < self.total_frames:
            if self.playing:
                ret, frame = self.cap.read()
                if ret:
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    h, w, c = frame.shape
                    qimage = QImage(frame.data, w, h, w * c, QImage.Format_RGB888)
                    self.frame_loaded.emit(qimage)
                    self.current_frame += 1
                self.msleep(frame_interval)
    
    

    def setVideoPosition(self, position):
        if hasattr(self, 'cap'):
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, position)
            self.current_frame = position

    def playPause(self):
        self.playing = not self.playing



class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(" Video Player ")

        
        self.isCameraOn = False
        self.isRecStart = False
        self.camera = Camera(self)
        self.camera.daemon = True
        self.record = Camera(self)
        self.record.daemon = True
        
        self.btn_camera.clicked.connect(self.clickCamera)
        self.camera.update.connect(self.updateCamera)
        self.btn_camera_rec.clicked.connect(self.clickRecord)
        self.record.update.connect(self.updateRecording)
        self.btn_camera_cap.clicked.connect(self.capture)


        self.off_camera()
        self.off_image()
        self.off_video()
        self.label_sign.hide()
        self.btn_image.clicked.connect(self.openFile)
        self.btn_image_pnt.clicked.connect(self.canpointer)
        self.btn_image_color.clicked.connect(self.inputColor)
        
        self.btn_clear.clicked.connect(self.changeRGB)
        self.btn_rgb.clicked.connect(self.changeRGB)
        self.btn_hsv.clicked.connect(self.changeHSV)

        self.btn_video.clicked.connect(self.openVFile)
        self.btn_video_ss.clicked.connect(self.playPause)
        self.slider_video.sliderMoved.connect(self.setVideoPosition)
        self.video_thread = None

        self.cnt = 0
        self.pixmap = QPixmap(self.label_viewer.width(), self.label_viewer.height())
        self.pixmap.fill(Qt.transparent)
        self.label_viewer.setPixmap(self.pixmap)
        self.x, self.y = None, None
        self.past_x, self.past_y = None, None
        
        self.colorr = ''
        
        
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
            self.btn_camera_rec.setText('Rec Stop')
            self.isRecStart = True
            
            self.recordingStart()
        else:
            self.btn_camera_rec.setText('Rec Start')
            self.isRecStart = False
            
            self.recordingStop()
            
    
    def recordingStart(self):
        self.record.running = True
        self.record.start()
        self.label_rec.show()

        
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
    
        
        
    def clickCamera(self):
        if self.isCameraOn == False:
            self.btn_camera.setText('Camera OFF')
            self.isCameraOn = True
            self.on_camera()
            self.off_image()
            self.off_video()
            self.cameraStart()
            
        else :
            self.btn_camera.setText('Camera ON')
            self.isCameraOn = False
            self.off_camera()
            
            self.cameraStop()
            self.recordingStop()


    def updateCamera(self):
        retval, image = self.video.read()
        if retval :
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
            h,w,c = image.shape
            qiamge = QImage(image.data, w, h, w*c, QImage.Format_RGB888)
            
            self.pixmap = self.pixmap.fromImage(qiamge)
            self.pixmap = self.pixmap.scaled(self.label_viewer.width(), self.label_viewer.height())
            
            self.label_viewer.setPixmap(self.pixmap)

    def cameraStart(self):
        self.camera.running = True
        self.camera.start()
        self.video = cv2.VideoCapture(-1)
        
    def cameraStop(self):
        self.camera.running = False
        self.video.release
    
    def on_video(self):
        self.slider_video.show()
        self.btn_video_ss.show()
        self.btn_video_rec.show()
    def off_video(self):
        self.slider_video.hide()
        self.btn_video_ss.hide()
        self.btn_video_rec.hide()
    
    
    def on_image(self):
        self.btn_image_pnt.show()
        self.btn_image_sq.show()
        self.btn_image_save.show()
        self.groupBox.show()
        self.btn_image_color.show()
        self.btn_clear.show()
    def off_image(self):
        self.btn_image_pnt.hide()
        self.btn_image_sq.hide()
        self.btn_image_save.hide()
        self.label_sign.hide()
        self.groupBox.hide()
        self.btn_image_color.hide()
        self.btn_clear.hide()
    
    
    def on_camera(self):
        self.btn_camera_rec.show()
        self.btn_camera_cap.show()
    def off_camera(self):
        self.label_rec.hide()
        self.btn_camera_rec.hide()
        self.btn_camera_cap.hide()
        
        
    
    def openVFile(self):
        file, _ = QFileDialog.getOpenFileName(filter='Video (*.mp4 *.avi *.mkv)')
        if file:
            if self.video_thread and self.video_thread.isRunning():
                self.video_thread.quit()
            self.video_thread = VideoThread(file)
            self.video_thread.frame_loaded.connect(self.showFrame)
            self.video_thread.start()
            self.on_video()
            self.off_image()
            self.off_camera()
            
            
    def showFrame(self, qimage):
        pixmap = QPixmap.fromImage(qimage)
        pixmap = pixmap.scaled(self.label_viewer.size(), Qt.KeepAspectRatio)
        self.label_viewer.setPixmap(pixmap)
        self.slider_video.setRange(0, self.video_thread.total_frames)
        self.slider_video.setValue(self.video_thread.current_frame)

        
    def playPause(self):
        if self.video_thread:
            self.video_thread.playPause()

    def setVideoPosition(self, position):
        if self.video_thread:
            self.video_thread.setVideoPosition(position)



    def inputColor(self):
        color = QColorDialog.getColor() # getColor() 사용시 OS 내장 컬러를 보여주고 선택할 수 있다.
        
        if color.isValid():
            self.colorr = color
            self.btn_image_color.setStyleSheet(f"background-color: {color.name()};")
        
        

    def changeHSV(self):
        mo_image =  self.moimage.copy()
        hsv = self.slider_hsv.value()
        H, S, V = cv2.split(mo_image)
        
        H = H + int(hsv)
        S = S + int(hsv)
        V = V + int(hsv)
        
        mo2_image = cv2.merge((H,S,V))
        h, w, c = mo2_image.shape
        qimage = QImage(mo2_image.data, w, h, w * c, QImage.Format_RGB888)
        self.pixmap = QPixmap.fromImage(qimage)
        self.pixmap = self.pixmap.scaled(self.label_viewer.size(), Qt.KeepAspectRatio)
        self.label_viewer.setPixmap(self.pixmap)
        
        
        
    def changeRGB(self):
        mo_image =  self.moimage.copy()
        red = self.lineEdit_r.text()
        green = self.lineEdit_g.text()
        blue = self.lineEdit_b.text()
        
        R,G,B = cv2.split(mo_image)
        
        R = R + int(red)
        G = G + int(green)
        B = B + int(blue)
        
        mo2_image = cv2.merge((R,G,B))
        h, w, c = mo2_image.shape
        qimage = QImage(mo2_image.data, w, h, w * c, QImage.Format_RGB888)
        self.pixmap = QPixmap.fromImage(qimage)
        self.pixmap = self.pixmap.scaled(self.label_viewer.size(), Qt.KeepAspectRatio)
        self.label_viewer.setPixmap(self.pixmap)
    
    
            
    def canpointer(self):
        self.cnt+=1
        if self.cnt%2==1:
            self.btn_image_pnt.setText('DRAW ON')
            self.label_sign.show()
        else : 
            self.btn_image_pnt.setText('DRAW OFF')
            self.label_sign.hide()
    
    
    
    def mouseMoveEvent(self, event):    # 누른 상태일 때 이벤트를 받음
        if self.x is None:
            self.x = event.x()
            self.y = event.y()
            return
        
        if self.cnt%2==1:
            painter = QPainter(self.label_viewer.pixmap())
            if self.colorr=='':
                self.pen = QPen(Qt.white, 3, Qt.SolidLine) 
            else:
                self.pen = QPen(self.colorr, 3, Qt.SolidLine) 
            painter.setPen(self.pen)
            painter.drawLine(self.x, self.y, event.x(), event.y())
            painter.end()
            self.update()
        
        self.x = event.x()
        self.y = event.y()
    
    
    
    def mouseReleaseEvent(self, event):     # 마우스를 떼면 초기화
        self.x = None
        self.y = None
        
        
        
    def openFile(self):
        file, _ = QFileDialog.getOpenFileName(filter='Image (*.*)')
        if file:
            image = cv2.imread(file)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            h, w, c = image.shape
            qimage = QImage(image.data, w, h, w * c, QImage.Format_RGB888)
            self.pixmap = QPixmap.fromImage(qimage)
            self.pixmap = self.pixmap.scaled(self.label_viewer.size(), Qt.KeepAspectRatio)
            self.label_viewer.setPixmap(self.pixmap)
            self.moimage = image
            
            self.on_image()
            self.off_camera()
            self.off_video()



if __name__ == "__main__": 
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec_())