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

        # コンボボックス欄の入力を有効
        combobox.setEditable(True)


# アプリの実行と終了
app = QtWidgets.QApplication()
window = MainWindow()
window.show()
app.exec_()
