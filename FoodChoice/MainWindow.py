import sys
import random
from PyQt5.QtWidgets import *
from listFiltering import veganistfiltering, al_listfiltering, people_listfiltering, kind_listfiltering
from SubWindow import *


class Main(QWidget) :

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self) :

        groupBox1 = QGroupBox("비건 / 논 비건", self)

        self.choose1Edit1 = QRadioButton('Vegan', self)
        self.choose1Edit2 = QRadioButton('Non_Vegan', self)

        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.choose1Edit1)
        vbox1.addWidget(self.choose1Edit2)
        groupBox1.setLayout(vbox1)
        groupBox1.setMinimumWidth(130)


        groupBox2 = QGroupBox("알레르기", self)

        self.choose2Edit1 = QCheckBox('없음')
        self.choose2Edit2 = QCheckBox('우유')
        self.choose2Edit3 = QCheckBox('견과류')
        self.choose2Edit4 = QCheckBox('갑각류')

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

        self.choose4Edit1 = QCheckBox('한식')
        self.choose4Edit2 = QCheckBox('중식')
        self.choose4Edit3 = QCheckBox('일식')
        self.choose4Edit4 = QCheckBox('양식')
        self.choose4Edit5 = QCheckBox('분식')
        self.choose4Edit6 = QCheckBox('동남아')

        vbox4 = QVBoxLayout()
        vbox4.addWidget(self.choose4Edit1)
        vbox4.addWidget(self.choose4Edit2)
        vbox4.addWidget(self.choose4Edit3)
        vbox4.addWidget(self.choose4Edit4)
        vbox4.addWidget(self.choose4Edit5)
        vbox4.addWidget(self.choose4Edit6)
        groupBox4.setLayout(vbox4)
        groupBox4.setMinimumWidth(130)

        self.viewer = QListWidget(self)
        self.meal_explain = QTextEdit()
        self.meal_explain.setReadOnly(True)


        FindButton = QPushButton("Find")
        FindButton.clicked.connect(self.buttonClicked)

        RandomButton = QPushButton("Random")
        RandomButton.clicked.connect(self.buttonClicked)

        AddButton = QPushButton("Add Food")
        AddButton.clicked.connect(self.buttonClicked)

        randommeal = QLabel("추천 음식 :")
        self.random_meal = QLabel("")


        grid = QGridLayout()
        grid.addWidget(groupBox1, 0, 0)
        grid.addWidget(groupBox2, 0, 2)
        grid.addWidget(groupBox3, 1, 0)
        grid.addWidget(self.meal_explain, 0, 1, 2, 1)
        grid.addWidget(groupBox4, 1, 2)
        grid.addWidget(randommeal, 2, 0)
        grid.addWidget(self.random_meal, 2, 1)
        grid.addWidget(self.viewer, 3, 0, 1, 3)
        grid.addWidget(AddButton, 4, 0)
        grid.addWidget(RandomButton, 4, 1)
        grid.addWidget(FindButton, 4, 2)

        self.setLayout(grid)

        self.setGeometry(800, 300, 600, 600)
        self.setWindowTitle('Food Choice')
        self.show()



    def buttonClicked(self) :
        sender = self.sender


        if sender().text() == "Find":
            self.meal_list = []  # 최종적으로 필터링된 음식들에 대한 리스트

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


            if self.choose1Edit1.isChecked():
                al_listfiltering(veganistfiltering(self.choose1Edit1.text()), ar, self.meal_list)    #알레르기 필터링 함수
                for i in self.meal_list[:]:
                    people_listfiltering(i, meal, veganistfiltering(self.choose1Edit1.text()), self.meal_list)   #인분 필터링 함수
                for i in self.meal_list[:]:
                    kind_listfiltering(i, kind, veganistfiltering(self.choose1Edit1.text()), self.meal_list)   #음식종류 필터링 함수
            elif self.choose1Edit2.isChecked():
                al_listfiltering(veganistfiltering(self.choose1Edit2.text()), ar, self.meal_list)  # 알레르기 필터링 함수
                for i in self.meal_list[:]:
                    people_listfiltering(i, meal, veganistfiltering(self.choose1Edit2.text()), self.meal_list)  # 인분 필터링 함수
                for i in self.meal_list[:]:
                    kind_listfiltering(i, kind, veganistfiltering(self.choose1Edit2.text()), self.meal_list)  # 음식종류 필터링 함수



            self.viewer.clear()
            for f in self.meal_list:
                self.viewer.addItem(f)

            self.viewer.itemClicked.connect(self.mealExplain)

        elif sender().text() == "Random" :
            try :
                if len(self.meal_list) > 5:
                    self.random_meal.setText(random.choice(self.meal_list))
                else:
                    self.random_meal.setText("")

            except :

                self.random_meal.setText("Please Click FindButton First!")




        elif sender().text() == "Add Food" :
            ex = SubWindow()
            r = ex.showModal()


    def mealExplain(self):
        dbfilename = 'meal_explain.txt'

        fH = open(dbfilename, 'r')
        line = fH.read()
        fH.close()
        meal_Explain = eval(line)
        explain = self.viewer.currentItem()
        if explain.text() in meal_Explain:
            self.meal_explain.setText(meal_Explain[explain.text()])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec_())
