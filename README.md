# pyQt_Git

python과 pyQt5 Designer 연습

1. 계산기

2. TextBrowser 
    0. self.lineEdit.returnPressed.connect >> 엔터키 입력받는 방법
    1. lineEdit에 쓴 문자열 가져오기 : self.lineEdit.text()  <!-- 그냥 text() -->
    2. lineEdit 지우기 : self.lineEdit.setText("")   <!-- setText("")보단 clear() -->
    3. textBrowser 문자열 가져오기 : self.textBrowser.toPlainText()  <!-- toPlainText() -->
    4. textBrowser에 문자열 추가 : self.textBrowser.append(txt)  <!-- 전 문자열에 추가하는거라고 toPlainText().append() 처럼 하진 않음.-->

3. TextEdit
    1. 1. textEdit에 쓴 문자열 가져오기 : self.lineEdit.toPlainText()  <!-- text() 아님. line만 text(). -->