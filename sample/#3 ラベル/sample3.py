# PySide2のモジュールを読み込む
from PySide2 import QtWidgets, QtGui


# ウィンドウの見た目と各機能
class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 650, 300)

        # Qt Style Sheets (CSS風) で見た目を設定
        label_style = """QLabel {
            color: #FF00AA;                 /* 文字色 */
            font-size: 128px;               /* 文字サイズ */
            background-color: yellow;       /* 背景色 */
            font-family: 851CHIKARA-YOWAKU; /* フォント（文字の輪郭） */
        }"""

        label = QtWidgets.QLabel(self)   # ラベルオブジェクトの生成
        label.setStyleSheet(label_style) # 指定したフォントを反映
        label.setText("腹ン中が\nパンパンだぜ")  # 適当な文字を表示


# アプリの実行と終了
app = QtWidgets.QApplication()
window = MainWindow()
window.show()
app.exec_()
