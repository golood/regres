from PyQt5 import QtWidgets
from UI.mainWindow import Ui_MainWindow
from UI.window1 import Ui_Dialog
import sys


class MyDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self, parent.ui.data)

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_3.clicked.connect(self.openDialog)

    def openDialog(self):
        dialog = MyDialog(self)
        dialog.exec_()

app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())