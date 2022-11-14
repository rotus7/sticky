# PySide2のモジュールを読み込む
from PySide2 import QtWidgets


# ウィンドウの見た目と各機能（今はウィンドウだけ）
class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()


# アプリの実行と終了
app = QtWidgets.QApplication()
window = MainWindow()
window.show()
app.exec_()
