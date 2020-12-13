import sys
import random
from PyQt5.QtWidgets import *
from listFiltering import veganistfiltering, al_listfiltering, people_listfiltering, kind_listfiltering


class SubWindow(QDialog) :
    def __init__(self):
        super().__init__()
        self.initUI()



    def initUI(self):

        self.setWindowTitle('Add Food')
        self.setGeometry(700, 300, 300, 300)
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        vbox = QVBoxLayout()

        add1 = QLabel("음식 이름: ")
        self.add_1 = QLineEdit("원하는 음식의 이름을 적어주세요!")
        add2 = QLabel("음식 설명: ")
        self.add_2 = QTextEdit("칼로리를 함께 적어주세요!")

        AddButton = QPushButton('Add')
        AddButton.clicked.connect(self.AddFood)

        groupBox1 = QGroupBox("비건 / 논 비건", self)

        self.choose1Edit1 = QRadioButton('Vegan', self)
        self.choose1Edit2 = QRadioButton('Non_Vegan', self)

        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.choose1Edit1)
        vbox1.addWidget(self.choose1Edit2)
        groupBox1.setLayout(vbox1)
        groupBox1.setMinimumWidth(130)



        groupBox2 = QGroupBox("알레르기", self)

        self.choose2Edit1 = QRadioButton('없음')
        self.choose2Edit2 = QRadioButton('우유')
        self.choose2Edit3 = QRadioButton('견과류')
        self.choose2Edit4 = QRadioButton('갑각류')

        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.choose2Edit1)
        vbox2.addWidget(self.choose2Edit2)
        vbox2.addWidget(self.choose2Edit3)
        vbox2.addWidget(self.choose2Edit4)

        groupBox2.setLayout(vbox2)
        groupBox2.setMinimumWidth(130)


        groupBox3 = QGroupBox("몇 인분 식사", self)

        self.choose3Edit1 = QRadioButton('1인용', self)
        self.choose3Edit2 = QRadioButton('2인용', self)

        vbox3 = QVBoxLayout()
        vbox3.addWidget(self.choose3Edit1)
        vbox3.addWidget(self.choose3Edit2)
        groupBox3.setLayout(vbox3)
        groupBox3.setMinimumWidth(130)


        groupBox4 = QGroupBox("음식 종류", self)

        self.choose4Edit1 = QRadioButton('한식')
        self.choose4Edit2 = QRadioButton('중식')
        self.choose4Edit3 = QRadioButton('일식')
        self.choose4Edit4 = QRadioButton('양식')
        self.choose4Edit5 = QRadioButton('분식')
        self.choose4Edit6 = QRadioButton('동남아')

        vbox4 = QVBoxLayout()
        vbox4.addWidget(self.choose4Edit1)
        vbox4.addWidget(self.choose4Edit2)
        vbox4.addWidget(self.choose4Edit3)
        vbox4.addWidget(self.choose4Edit4)
        vbox4.addWidget(self.choose4Edit5)
        vbox4.addWidget(self.choose4Edit6)
        groupBox4.setLayout(vbox4)
        groupBox4.setMinimumWidth(130)

        grid = QGridLayout()
        grid.addWidget(groupBox1, 0, 0)
        grid.addWidget(groupBox2, 0, 1)
        grid.addWidget(groupBox3, 1, 0)
        grid.addWidget(groupBox4, 1, 1)
        grid.addWidget(add1, 2, 0)
        grid.addWidget(self.add_1, 2, 1)
        grid.addWidget(add2, 3, 0)
        grid.addWidget(self.add_2, 3, 1)
        grid.addWidget(AddButton, 4, 0, 1, 2)

        self.setLayout(grid)

        self.setGeometry(800, 300, 600, 600)
        self.setWindowTitle('Food Choice')
        self.show()


    def showModal(self):
        return super().exec_()



    def AddFood(self):
        ar = ""
        if self.choose2Edit1.isChecked():
            ar = self.choose2Edit1.text()
        elif self.choose2Edit2.isChecked():
            ar = self.choose2Edit2.text()
        elif self.choose2Edit3.isChecked():
            ar = self.choose2Edit3.text()
        elif self.choose2Edit4.isChecked():
            ar = self.choose2Edit4.text()

        meal = ""
        if self.choose3Edit1.isChecked():
            meal = self.choose3Edit1.text()
        elif self.choose3Edit2.isChecked():
            meal = self.choose3Edit2.text()

        kind = ""
        if self.choose4Edit1.isChecked():
            kind = self.choose4Edit1.text()
        elif self.choose4Edit2.isChecked():
            kind = self.choose4Edit2.text()
        elif self.choose4Edit3.isChecked():
            kind = self.choose4Edit3.text()
        elif self.choose4Edit4.isChecked():
            kind = self.choose4Edit4.text()
        elif self.choose4Edit5.isChecked():
            kind = self.choose4Edit5.text()
        elif self.choose4Edit6.isChecked():
            kind = self.choose4Edit6.text()



        if self.choose1Edit1.isChecked() :
            dbfilename = 'vegan_meal.txt'

            fH = open(dbfilename, 'r')
            line = fH.read()
            fH.close()
            vegan_meal = eval(line)

            dbfilename_1 = 'meal_explain.txt'

            fH = open(dbfilename_1, 'r')
            line = fH.read()
            fH.close()
            meal_Explain = eval(line)


            vegan_meal.update({self.add_1.text() : {'알레르기': ar, '인용': meal, '종류': kind}})
            meal_Explain.update({self.add_1.text() : self.add_2.toPlainText()})

            fH = open(dbfilename, 'w')
            fH.write(str(vegan_meal))
            fH.close()

            fH = open(dbfilename_1, 'w')
            fH.write(str(meal_Explain))
            fH.close()

            self.add_1.setText("원하는 음식의 이름을 적어주세요!")
            self.add_2.setText("칼로리를 함께 적어주세요!")



        else :
            dbfilename = 'non_vegan_meal.txt'

            fH = open(dbfilename, 'r')
            line = fH.read()
            fH.close()
            non_vegan_meal = eval(line)

            dbfilename_1 = 'meal_explain.txt'

            fH = open(dbfilename_1, 'r')
            line = fH.read()
            fH.close()
            meal_Explain = eval(line)

            non_vegan_meal.update({self.add_1.text(): {'알레르기': ar, '인용': meal, '종류': kind}})
            meal_Explain.update({self.add_1.text(): self.add_2.toPlainText()})

            fH = open(dbfilename, 'w')
            fH.write(str(non_vegan_meal))
            fH.close()

            fH = open(dbfilename_1, 'w')
            fH.write(str(meal_Explain))
            fH.close()

            self.add_1.setText("원하는 음식의 이름을 적어주세요!")
            self.add_2.setText("칼로리를 함께 적어주세요!")