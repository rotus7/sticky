# PySide2のモジュールを読み込む
from PySide2 import QtWidgets


# ウィンドウの見た目と各機能
class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # コンボボックスオブジェクトの生成
        self.combobox = QtWidgets.QComboBox(self)

        # コンボボックスの選択肢を追加
        self.combobox.addItems(["One", "Two", "Three"])

        # コンボボックスの選択肢が変更されたら呼び出す関数
        self.combobox.currentIndexChanged.connect(self.notice_changed)

    # 呼び出される関数
    def notice_changed(self):
        print("Changed!!")


# アプリの実行と終了
app = QtWidgets.QApplication()
window = MainWindow()
window.show()
app.exec_()
