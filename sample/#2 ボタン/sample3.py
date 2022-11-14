# PySide2のモジュールを読み込む
from PySide2 import QtWidgets


# ウィンドウの見た目と各機能
class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        button1 = QtWidgets.QPushButton("Button 1", self)
        button1.clicked.connect(self.pushed_button1)

    def pushed_button1(self):
        print("ﾊﾞﾝ（∩`･ω･）ﾊﾞﾝﾊﾞﾝ \n  ＿/_ﾐつ/￣￣￣/\n       ＼/＿＿＿/”")


# アプリの実行と終了
app = QtWidgets.QApplication()
window = MainWindow()
window.show()
app.exec_()
