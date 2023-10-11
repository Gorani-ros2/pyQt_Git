import sys
import pandas as pd
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic


from_class = uic.loadUiType("calculator.ui")[0]

## 결과값에 천자리 구분쉼표, 찍기
## 소수점 이하 5자리 이상이면 5자리이상 버림 => 4자리까지만 출력
def make_rest(N):
    if '.' not in N:
        li = []
        for i in range(len(N)):
            li.append(N[i])
        for i in range(len(N)//3):
            li.insert(-4*(i)-3,',')
    else :
        # 소수점이 있는 경우 소수점을 기준으로 분리
        f_N,b_N = N.split('.')
        li = []
        if len(b_N) > 4 :
            b_N = b_N[:4]
        else :
            pass
        
        for i in range(len(f_N)):
            li.append(f_N[i])
        for i in range(len(f_N)//3):
            li.insert(-4*(i)-3,',')

        li+=('.')
        li+=b_N


    if li[0]==',' or li[:2]== ['-', ',']:
        li.remove(',')
    re_N = ''
    for i in li:
        re_N+=(i)
    return re_N
    
    
    
        
class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Calculator !")
        
        # 0 1 2 3 4 5 6 7 8 9
        self.pushButton_0.clicked.connect(self.add_text)
        self.pushButton_1.clicked.connect(self.add_text)
        self.pushButton_2.clicked.connect(self.add_text)
        self.pushButton_3.clicked.connect(self.add_text)
        self.pushButton_4.clicked.connect(self.add_text)
        self.pushButton_5.clicked.connect(self.add_text)
        self.pushButton_6.clicked.connect(self.add_text)
        self.pushButton_7.clicked.connect(self.add_text)
        self.pushButton_8.clicked.connect(self.add_text)
        self.pushButton_9.clicked.connect(self.add_text)
        
        # + - * /
        self.pushButton_add.clicked.connect(self.operator)
        self.pushButton_sub.clicked.connect(self.operator)
        self.pushButton_mul.clicked.connect(self.operator)
        self.pushButton_div.clicked.connect(self.operator)
        
        # .
        self.pushButton_dot.clicked.connect(self.dot_acting)
        # =
        self.pushButton_result.clicked.connect(self.result)
        # C
        self.pushButton_clear.clicked.connect(self.clearing)
        # ↼
        self.pushButton_delete.clicked.connect(self.delete)
        
        self.allow_dot = True  # 소수점 출력가능여부로 operator함수와 dot함수에서 쓰임
        self.N = 0
        
    ## 숫자 0 ~ 9
        # 초기값이 0이 아닌경우 기존값에 버튼값을 추가해서 출력
        # 초기값이 0이 아니면서 바로앞문자가 사칙연산인 경우
            # 입력값이 0이 아니라면 출력
            # 0이면 pass
        # 사칙연산 뒤에 0 입력불가
        # 초기값이 0인경우
            # 입력값이 0이 아니라면 출력
            # 0이면 pass
    def add_text(self):
        sending_button = self.sender().text()
        before_text = self.lineEdit_print.text()
        if before_text != '0' and before_text[-1] not in ['+','-','*','/'] :
            self.lineEdit_print.setText(f'{before_text+sending_button}')
        elif before_text[-1] in ['+','-','*','/'] :
            if sending_button == '0':
                pass
            else :
                self.lineEdit_print.setText(f'{before_text+sending_button}')
        else :
            if sending_button != '0' :
                self.lineEdit_print.setText(f'{sending_button}')
            else:
                pass
            
            
    ## 사칙연산 + - * /
        ## 숫자가 먼저 나와야 출력
            ## 바로 전 문자가 사칙연산이 아닐 경우에만 출력.        
            ## 바로전 문자가 .인경우 0을 붙여서 출력
            ## 바로 전 문자가 사칙연산인 경우 새로 출력
    def operator(self):
        sending_button = self.sender().text()
        before_text = self.lineEdit_print.text()
        if before_text:
            if before_text[-1] not in ['+','-','*','/','.'] :
                self.lineEdit_print.setText(f'{before_text+sending_button}')
                self.allow_dot = True
            elif before_text[-1] == '.':
                self.lineEdit_print.setText(f'{before_text+"0"+sending_button}')
                self.allow_dot = True
            else:
                self.lineEdit_print.setText(f'{before_text[:-1]+sending_button}')
                self.allow_dot = True
        else:
            pass
        
        
    # 소수점 .
        # 값이 있는 상태에서 누르면 . 출력
        # 사칙연산 뒤에 닷을 누르면 0. 출력
        # 초기상태에서 닷 누르면 0. 출력     
        # 사칙연산이 쓰인경우에만 추가로 쓸 수 있다. 
            # bool타입 allow_dot변수를 operator 함수에 사용
    def dot_acting(self):
        before_text = self.lineEdit_print.text()
        if before_text != '0' and self.allow_dot:
            if before_text[-1] not in ['+','-','*','/','.'] :
                self.lineEdit_print.setText(f'{before_text}.')
                self.allow_dot = False
            elif before_text[-1] in ['+','-','*','/']:
                self.lineEdit_print.setText(f'{before_text}0.')
                self.allow_dot = False
            else:
                pass
        elif before_text == '0':
            self.lineEdit_print.setText('0.')
            self.allow_dot = False
        else:
            pass
        
    
    # 삭제 <-
        # 직전자리까지만 출력
        # 1자리만 남은경우 0으로 출력
        # dot을 지운경우 allow_dot를 True로 변환해서 재허용
    def delete(self):
        before_text = self.lineEdit_print.text()
        if len(before_text) == 1:
            self.lineEdit_print.setText('0')
        else:
            self.lineEdit_print.setText(f'{before_text[:-1]}')
        if before_text[-1] == '.':
            self.allow_dot = True
    
    # 결과 =
        # 마지막 글자가 사칙연산이나 소수점인 경우는 계산에서 마지막글자를 제외
        # 스트링의 결과값을 eval로 계산.
        # 계산값을 lineEdit_result에 출력
        # -9999조~9999조를 벗어나면 OVERFLOW MIN/MAX 출력
        # 20자리를 넘으면 OVERFLOW LENGTH
    def result(self):
        check = 0  # 결과값 
        min = -9999999999999999
        max = 9999999999999999
        before_text = self.lineEdit_print.text()
        if before_text[-1] in ['+','-','*','/','.'] :
            check = eval(before_text[:-1])
        else:
            check = eval(before_text)
            
        if len(make_rest(str(check))) > 22:
            self.lineEdit_result.setText('OVERFLOW : LENGTH')  
        elif min <= check <= max:
            self.lineEdit_result.setText(f'{make_rest(str(check))}')
        else :
            if check >= max:
                self.lineEdit_result.setText('OVERFLOW : MAX')
            elif min >= check:
                self.lineEdit_result.setText('OVERFLOW : MIN')
            
            
    # 클리어 C
        # 라벨을 0으로 출력
    def clearing(self):
        self.lineEdit_print.setText('0')
        



if __name__ == "__main__":      # 프로그램을 실행하면 메인부터 실행됨.
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec_())