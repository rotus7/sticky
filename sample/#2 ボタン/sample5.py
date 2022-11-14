# PySide2のモジュールを読み込む
from PySide2 import QtWidgets


# ウィンドウの見た目と各機能（今はウィンドウだけ）
class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 300, 200)

        quitButton = QtWidgets.QPushButton("アプリを終了する", self)
        quitButton.clicked.connect(self.application_quit)

    def application_quit(self):
        # Qtが用意しているcloseスロットを実行
        self.close()


# アプリの実行と終了
app = QtWidgets.QApplication()
window = MainWindow()
window.show()
app.exec_()
