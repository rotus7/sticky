from PySide2 import QtWidgets


class Memo():
    id = 0
    text = ""
    left = 0
    top = 0
    width = 0
    height = 0


class MemoListNode():
    data = Memo()
    prevNode = None
    nextNode = None


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 1500, 1000)


app = QtWidgets.QApplication()
window = MainWindow()
window.show()
app.exec_()
