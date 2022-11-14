# PySide2のモジュールを読み込む
from PySide2 import QtWidgets


# ウィンドウの見た目と各機能
class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        label = QtWidgets.QLabel(self) # ラベルオブジェクトの生成
        label.setText("こんにちは。")    # 文字列としてラベルを表示


# アプリの実行と終了
app = QtWidgets.QApplication()
window = MainWindow()
window.show()
app.exec_()
