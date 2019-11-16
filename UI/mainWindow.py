# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from UI.window1 import Ui_Dialog

class Ui_Dialog(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(Ui_Dialog, self).__init__(parent)

        self.main = parent
        self.setObjectName("Dialog")
        self.resize(639, 344)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(
            QtCore.QRect(280, 300, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(
            QtCore.QRect(20, 20, 251, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(
            QtCore.QRect(288, 80, 71, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(
            QtCore.QRect(290, 120, 71, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.listWidget = QtWidgets.QListWidget(self)
        self.listWidget.setGeometry(
            QtCore.QRect(20, 80, 256, 192))
        self.listWidget.setObjectName("listWidget")

        self.listWidget_2 = QtWidgets.QListWidget(self)
        self.listWidget_2.setGeometry(
            QtCore.QRect(370, 80, 256, 192))
        self.listWidget_2.setObjectName("listWidget_2")

        self.retranslateUi(self)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Случайным образом"))
        self.pushButton_2.setText(_translate("Dialog", ">"))
        self.pushButton_3.setText(_translate("Dialog", "<"))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.setSortingEnabled(__sortingEnabled)

        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        self.listWidget_2.setSortingEnabled(__sortingEnabled)

    def randomDataAction(self):
        pass

    def rightColumnAction(self, item):
        pass

    def leftColumnAction(self, item):
        pass


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
        self.pushButton_3.clicked.connect(self.openDialog)

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
        dialog = Ui_Dialog(self)
        dialog.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Загрузить"))
        self.label.setText(_translate("MainWindow", "Loaded File..."))
        self.pushButton_2.setText(_translate("MainWindow", "Выбрать зависимую переменную"))
        self.pushButton_3.setText(_translate("MainWindow", "Разделить матрицу"))
        self.pushButton_4.setText(_translate("MainWindow", "Выбрать рабочую матрицу"))

    def showInputDialog1(self):

        text, ok = QtWidgets.QInputDialog.getText(self,
                    'Диалог выбора рабочей матрицы',
                    'Введите через пробел номера столбцов')
        if ok:
            self.number = list(map(int, text.split()))
            self.number = list(map(lambda x: x - 1, self.number))
            self._initWorkMatrix()
            self._set_data_in_table(self.workMatrix)

    def showInputDialog(self):

        number, ok = QtWidgets.QInputDialog.getInt(self,
                    'Диалог выбора зависимой переменной',
                    'Введите номер столбца с зависимой переменной')

        self.zav_var = number
        if ok:
            if number >= 0 & number < len(self.data[0]):
                self._initHeadersLabels(number - 1)

    def _initHeadersLabels(self, index):
        headersLabels = []

        num = 0
        for i in range(len(self.workMatrix[0])):
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

        self.workMatrix = self.data
        self._set_data_in_table(self.data)

    def initTableH1(self):
        pass

    def initTableH2(self):
        pass

    def _set_data_in_table(self, data):
        self.tableWidget.clear()

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
                if index in self.number:
                    new_line.append(item)
                index += 1
            self.workMatrix.append(new_line)
