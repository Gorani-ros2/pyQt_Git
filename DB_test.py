import sys
import mysql.connector
import pandas as pd

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5.QtCore import QDate

from_class = uic.loadUiType("DB_test.ui")[0]

def li_re():
    l1 = []
    return l1

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(" DB Connect Test")
        
        self.pushButton.clicked.connect(self.search)        
        self.pushButton_2.clicked.connect(self.conGen)
        self.pushButton_3.clicked.connect(self.conJob)
        self.pushButton_4.clicked.connect(self.conAcy)
        
    def conGen(self):
        self.genderBox.addItem('All') 
        pd = self.dbconnect('select distinct sex from celeb;')
        for m in pd[0]:
            self.genderBox.addItem(str(m)) 
            
            
    def conJob(self):
        self.jobBox.addItem('All') 
        pd = self.dbconnect('select distinct job_title from celeb;')
        a = []
        for i in pd[0]:
            if ',' in i:
                a.append(i.split(', ')[0])
                a.append(i.split(', ')[1])
            else :
                a.append(i)
        a = list(set(a))
        for m in a:
            self.jobBox.addItem(str(m)) 
            
            
            
    def conAcy(self):
        self.agencyBox.addItem('All') 
        pd = self.dbconnect('select distinct agency from celeb;')
        for m in pd[0]:
            self.agencyBox.addItem(str(m)) 
            
                    

    def dbconnect(self,df):
        li = []
        amazon = mysql.connector.connect(
            host = "database-1.ca4ikbv2yxyc.ap-northeast-2.rds.amazonaws.com",
            port = 3306,
            user = "gorani",
            password = "1",
            database = "amrbase"
        )
        cur = amazon.cursor(buffered = True)  # 읽어올 데이터 양이 많은 경우 buffered = True
        cur.execute(df)
        result = cur.fetchall()
        for a in result :
            li.append(a)
        test_pd = pd.DataFrame(li)
        amazon.close()    
        return test_pd
            
            
            
            
    def search(self):
        gb = self.genderBox.currentText()
        jb = self.jobBox.currentText()
        ab = self.agencyBox.currentText()

        b1 = str(self.dateEdit.date().toString("yyyy-MM-dd"))
        b2 = str(self.dateEdit_2.date().toString("yyyy-MM-dd"))

        tt = [gb,jb,ab]
        for i in range(len(tt)):
            if tt[i] == 'All' :
                tt[i] = '' 
            else:
                pass
        test_pd = self.dbconnect(f'''select * from celeb where sex like "%{tt[0]}%" and job_title like "%{tt[1]}%" and agency like "%{tt[2]}%" and (birthday between "{b1}" and "{b2}");''')

        self.tableWidget.setRowCount(len(test_pd))
        if len(test_pd) > 1:
            for i in range(len(test_pd)):
                for j in range(len(test_pd.columns)):
                    self.tableWidget.setItem(i,j,QTableWidgetItem(str(test_pd.iloc[i][j])))
        else :
            for j in range(len(test_pd.columns)):
                    self.tableWidget.setItem(0,j,QTableWidgetItem(str(test_pd.iloc[0][j])))


if __name__ == "__main__": 
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec_())