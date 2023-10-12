# pyQt_Git

---

python과 pyQt5 Designer 연습

1. 계산기

<br>

2. TextBrowser  <br>
    1. ``` self.lineEdit.returnPressed.connect``` >> 엔터키 입력받는 방법
    2. lineEdit에 쓴 문자열 가져오기 : ```  self.lineEdit.text()  ## 그냥 text()  ```
    3. lineEdit 지우기 : ```  self.lineEdit.setText("")  ## setText("")보단 clear() ```
    4. textBrowser 문자열 가져오기 : ```  self.textBrowser.toPlainText() ## toPlainText() ```
    5. textBrowser에 문자열 추가 : ```  self.textBrowser.append(txt) ``` <br>
                ```## 전 문자열에 추가하는거라고 toPlainText().append() 처럼 하진 않음 ```

<br>

3. TextEdit <br>
    1. **setTextColor**함수나 **setFont** 함수를 새로 정의한다고 해서 이름 바꿔 써도 되는게 아님. 이 대소문자 그대로 써야함.
    2. textEdit에 쓴 문자열 가져오기 : ```  self.lineEdit.toPlainText() ## text() 아님. line만 text(). ``` 
    3. 폰트바꾸는 것과 달리, 폰트사이즈와 폰트색상변경 할 때는 문자열 선택이 필요하다.
        1. ```  self.textEdit_2.selectAll() ## 전체선택하고  ``` 
        2. ```  self.textEdit_2.setTextColor(color) ```또는 <br>
        &nbsp;``` self.textEdit_2.setFontPointSize(size) ## 색상을 입히거나 폰트를 변경하고  ```
        3. ```  self.textEdit_2.moveCursor(QTextCursor.End)  ## 선택 초기화 ```

<br>

4. Dialog
   1. 팝업창 다이얼로그 QMessageBox.question <br>

    ```python
    text = self.lineEdit.text() 
    text.isdigit()
    retval = QMessageBox.question(self, 'QMessageBox - ?', 'Are you sure?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)  # ???
    ```
   2. 파일열기 QFileDialog.getOpenFileName
   ```python
   QFileDialog.getOpenFileName(self, 'ㅍㅇ ㅇㄱ', './')
   if name[0]:  # [0] ???
            with open(name[0], 'r') as file:  # 'r' ???
                data = file.read()
                self.textEdit.setText(data)
   ```
   3. 내장폰트 다이얼로그 QFontDialog.getFont
   ```python
   font, ok = QFontDialog.getFont()  # 내장 폰트를 보여주고 선택할 수 있다.
   if ok and font:
   ```
   4. 내장컬러 다이얼로그 QColorDialog.getColor()
    ```python
    color = QColorDialog.getColor() # getColor() 사용시 OS 내장 컬러를 보여주고 선택할 수 있다.    
        if color.isValid():
    ```
   5. 인풋 다이얼로그
   ```python
   text, ok = QInputDialog.getText(self, 'QInput - Name', 'What`s your name ?')
   ```
   6. 목록 다이얼로그 QInputDialog.getItem
   ```python
    items = ['봄', '여름', '가을', '겨울']
    item, ok = QInputDialog.getItem(self, 'QInput - Season', 'Choose your favorite Season.', items, 0, False)  # 0과 False의 의미 확인하기 
    if ok and item:
        self.textEdit.append(item)
   ```

