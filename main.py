import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sip


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


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setGeometry(300, 50, 400, 350)
        self.setWindowTitle("Sticky")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
