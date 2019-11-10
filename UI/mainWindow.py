# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from UI.window1 import Ui_Dialog


class Ui_MainWindow(QtWidgets.QMainWindow):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 10, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.loadFile)

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 50, 771, 192))
        self.tableWidget.setObjectName("tableWidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 10, 400, 21))
        self.label.setObjectName("label")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 260, 261, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.showInputDialog)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 300, 261, 25))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(280, 260, 261, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.showInputDialog1)


        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(670, 530, 118, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def openDialog(self):
        self.dialog.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Загрузить"))
        self.label.setText(_translate("MainWindow", "Loaded File..."))
        self.pushButton_2.setText(_translate("MainWindow", "Выбрать зависимую переменную"))
        self.pushButton_3.setText(_translate("MainWindow", "Разделить матрицу"))
        self.pushButton_4.setText(_translate("MainWindow", "Выбрать независимые переменные"))

    def showInputDialog1(self):

        text, ok = QtWidgets.QInputDialog.getText(self,
                    'Диалог выбора независимых переменных',
                    'Введите через пробел столбцы с независимыми переменными')
        if ok:
            self.number = list(map(int, text.split()))

    def showInputDialog(self):

        number, ok = QtWidgets.QInputDialog.getInt(self,
                    'Диалог выбора зависимой переменной',
                    'Введите номер столбца с зависимой переменной')

        self.zav_var = number
        if ok:
            if number >= 0 & number < len(self.data[0]):
                self._initHeadersLabels(number)

    def _initHeadersLabels(self, index):
        headersLabels = []

        num = 0
        for i in range(len(self.data[0])):
            if i != index:
                headersLabels.append('x' + str(num))
                num += 1
            else:
                headersLabels.append('y')

        self.tableWidget.setHorizontalHeaderLabels(headersLabels)

    def loadFile(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(
            self, 'Open File', '')

        self.data = []
        if fname[0] != '':
            self.label.setText(fname[0])
            with open(fname[0], 'r', encoding='utf-8') as f:
                for line in f:
                    self.data.append(list(map(float, line.split())))

        self._set_data_in_table(self.data)

    def _set_data_in_table(self, data):
        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(len(data[0]))

        row = 0
        for line in data:
            col = 0

            for item in line:
                cellinfo = QtWidgets.QTableWidgetItem(str(item))
                self.tableWidget.setItem(row, col, cellinfo)
                col += 1

            row += 1

    def _initWorkMatrix(self):
        self.workMatrix = []

        for line in self.data:
            new_line = []
            index = 0
            for item in line:
                if index not in self.number:
                    new_line.append(item)
                index += 1
            self.workMatrix.append(new_line)
