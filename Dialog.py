import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic


from_class = uic.loadUiType("Dialog.ui")[0]

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(" Test - Multi Dialog ")
        
        self.btnName.clicked.connect(self.inputName)  # 입력값 다이얼로그
        self.btnSeason.clicked.connect(self.inputSeason) # 정해진 목록에서 선택
        self.btnColor.clicked.connect(self.inputColor) # 색상변경
        self.btnFont.clicked.connect(self.inputFont)
        self.btnFile.clicked.connect(self.openFile) 
        self.lineEdit.returnPressed.connect(self.question)


    def question(self):
        text = self.lineEdit.text()
        
        if text.isdigit():
            self.textEdit.setText(text)
        else:
            # QMessageBox.warning(self, 'QMessageBox - setText', 'Please enter only numbers.')
            # self.lineEdit.clear()
            retval = QMessageBox.question(self, 'QMessageBox - ?', 'Are you sure?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No) # 이게뭥미
            if retval == QMessageBox.Yes :
                self.textEdit.setText(text)
            else:
                self.lineEdit.clear()
                
        
    def openFile(self):
        name = QFileDialog.getOpenFileName(self, 'ㅍㅇ ㅇㄱ', './') # 진짜 많이씀. https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QFileDialog.html
        
        if name[0]:  # [0]의 의미
            with open(name[0], 'r') as file: # 'r' 의 의미
                data = file.read()
                self.textEdit.setText(data)
                
        
    def inputFont(self):
        font, ok = QFontDialog.getFont()  # 내장 폰트를 보여주고 선택할 수 있다.
        
        if ok and font:
            info = QFontInfo(font)  # class QFontInfo(PyQt5.sipsimplewrapper) 클래스 객체선언
            self.textEdit.append(info.family() + info.styleName())  # textEdit에는 폰트체 + 스타일이름을 출력
            self.textEdit.selectAll()
            self.textEdit.setFont(font)
            self.textEdit.moveCursor(QTextCursor.End)
            
        
    def inputColor(self):
        color = QColorDialog.getColor() # getColor() 사용시 OS 내장 컬러를 보여주고 선택할 수 있다.
        
        if color.isValid():
            self.textEdit.append('Color')
            self.textEdit.selectAll()
            self.textEdit.setTextColor(color)
            self.textEdit.moveCursor(QTextCursor.End)
    
    def inputSeason(self):
        # items와 item을 구별
        # get아이템은 목록으로 나옴
        items = ['봄', '여름', '가을', '겨울']
        item, ok = QInputDialog.getItem(self, 'QInput - Season', 'Choose your favorite Season.', items, 0, False)  # 0과 False의 의미 확인하기 
        if ok and item:
            self.textEdit.append(item)
        
        
    def inputName(self):
        # text : 입력한 데이터, ok : ok버튼
        text, ok = QInputDialog.getText(self, 'QInput - Name', 'What`s your name ?')
        
        if ok and text:
            # 값과 ok가 입력되면 입력값으로 textedit이 바뀌는게 아니라 append 됨
            self.textEdit.append(text)



if __name__ == "__main__": 
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec_())