# PySide2のモジュールを読み込む
from PySide2 import QtWidgets
from PySide2 import QtCore


# ウィンドウの見た目と各機能
class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 500, 300)

        # ラベルオブジェクトの生成とフォント設定
        self.label = QtWidgets.QLabel("チェックボックスの入力状態で表示が変化します。", self)
        self.setStyleSheet("QLabel { font-size: 24px; }")
        self.label.move(10, 100)

        # チェックボックスオブジェクトの生成と配置
        checkBox = QtWidgets.QCheckBox("Check me!!", self)
        checkBox.move(10, 10)

        # チェックボックスの入力状態に応じて関数を実行
        checkBox.stateChanged.connect(lambda: self.checkboxChange(checkBox.checkState()))


    # チェックされた瞬間に実行される関数（ラベルの色を変えるだけ）
    def checkboxChange(self, state):
        if state == QtCore.Qt.Checked:
            self.label.setStyleSheet("""QLabel {
                color: green;
                background-color: lime;
            }""")
            self.label.setText("チェックしました！！")
        elif state == QtCore.Qt.Unchecked:
            self.label.setStyleSheet("""QLabel {
                color: red;
                background-color: pink;
            }""")
            self.label.setText("チェックされていません・・・")
        else:
            self.label.setText("Unknown State.")


# アプリの実行と終了
app = QtWidgets.QApplication()
window = MainWindow()
window.show()
app.exec_()
