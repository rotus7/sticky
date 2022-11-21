# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from src.ui import Ui_Form
from src.func import const

# set max sticky-notes
const.MAX_STICKY = 8


class gui(QtWidgets.QDialog):
    def __init__(self, parent=None):
        # init
        super(gui, self).__init__(parent)

        # set class
        self.ui = Ui_Form()

        # create ui
        self.ui.setupUi(self)

    def reset(self):
        print("Hello")

