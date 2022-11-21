import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from src.ui import Ui_Form


class gui(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(gui, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def reset(self):
        print("Hello")


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon('image/sticky.ico'))
    window = gui()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
