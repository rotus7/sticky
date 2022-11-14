# PySide2のモジュールを読み込む
from PySide2 import QtWidgets, QtGui


# ウィンドウの見た目と各機能
class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 320, 229)

        # QMovie型でGIFファイルを取得
        movie = QtGui.QMovie(R"E:\Users\rotus\Pictures\Party Parrot.gif")
        # GIFファイルを再生
        movie.start()

        label = QtWidgets.QLabel(self) # ラベルオブジェクトの生成
        label.setMovie(movie)          # ウィンドウにGIFを表示


# アプリの実行と終了
app = QtWidgets.QApplication()
window = MainWindow()
window.show()
app.exec_()
