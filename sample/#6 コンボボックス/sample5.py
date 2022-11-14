# PySide2のモジュールを読み込む
from PySide2 import QtWidgets


# ウィンドウの見た目と各機能
class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # コンボボックスオブジェクトの生成
        combobox = QtWidgets.QComboBox(self)

        # コンボボックスの選択肢を追加
        combobox.addItems(["One", "Two", "Three"])

        # 真ん中の選択肢 "Two" を削除 (コンボボックスのIDで指定)
        combobox.removeItem(1)


# アプリの実行と終了
app = QtWidgets.QApplication()
window = MainWindow()
window.show()
app.exec_()
