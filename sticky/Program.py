# -*- coding: utf-8 -*-

from os.path import dirname, abspath
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from src.ctr import gui

import sys


def main():
    # set qt-app class
    app = QApplication(sys.argv)

    # set window icon
    app.setWindowIcon(QIcon('image/sticky.ico'))

    # set class (create window)
    window = gui()

    # show window
    window.show()

    # exit
    sys.exit(app.exec_())


if __name__ == '__main__':
    # get parent directory
    parent_dir = dirname(dirname(dirname(abspath(__file__))))

    if parent_dir not in sys.path:
        # set parent directory
        sys.path.append(parent_dir)

    main()
