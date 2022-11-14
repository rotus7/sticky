# PySide2のモジュールを読み込む
from PySide2 import QtWidgets, QtGui


# ウィンドウの見た目と各機能
class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 400, 400)

        # ラベルオブジェクトの生成
        label = QtWidgets.QLabel(self)
        # QPixmap型に変換してウィンドウに画像を表示
        label.setPixmap(QtGui.QPixmap(R"E:\Users\rotus\Pictures\eadcd23a-8b3b-4b24-a875-139fd7af517a_.jpg"))


# アプリの実行と終了
app = QtWidgets.QApplication()
window = MainWindow()
window.show()
app.exec_()
