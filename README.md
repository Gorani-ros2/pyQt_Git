# pyQt_Git

python과 pyQt5 Designer 연습

1. 계산기

2. TextBrowser 
    0. ```python self.lineEdit.returnPressed.connect``` >> 엔터키 입력받는 방법
    1. lineEdit에 쓴 문자열 가져오기 : ```python  self.lineEdit.text()  ## 그냥 text()  ```
    2. lineEdit 지우기 : ```python  self.lineEdit.setText("")  ## setText("")보단 clear() ```
    3. textBrowser 문자열 가져오기 : ```python  self.textBrowser.toPlainText() ## toPlainText() ```
    4. textBrowser에 문자열 추가 : ```python  self.textBrowser.append(txt) ``` <br>
                                ```## 전 문자열에 추가하는거라고 toPlainText().append() 처럼 하진 않음 ```

3. TextEdit
    0. **setTextColor**함수나 **setFont** 함수를 새로 정의한다고 해서 이름 바꿔 써도 되는게 아님. 이 대소문자 그대로 써야함.
    1. textEdit에 쓴 문자열 가져오기 : ```python  self.lineEdit.toPlainText() ## text() 아님. line만 text(). ``` 
    2. 폰트바꾸는 것과 달리, 폰트사이즈와 폰트색상변경 할 때는 문자열 선택이 필요하다.
        1. ```python  self.textEdit_2.selectAll() ## 전체선택하고 --> ``` 
        2. ```python  self.textEdit_2.setTextColor(color) ```또는 <br>
           ```python self.textEdit_2.setFontPointSize(size) ## 색상을 입히거나 폰트를 변경하고  ```
        4. ```python  self.textEdit_2.moveCursor(QTextCursor.End)  ## 선택 초기화 ```
