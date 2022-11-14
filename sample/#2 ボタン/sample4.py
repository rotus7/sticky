# PySide2のモジュールを読み込む
from PySide2 import QtWidgets


# ウィンドウの見た目と各機能
class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # メニューインスタンス生成（この変数menuListに項目と機能を追加していく）
        menuList = QtWidgets.QMenu(self)

        # 喜びのメニューとその機能を追加
        action = QtWidgets.QAction("喜", menuList)  # 喜のメニューを作成
        action.setObjectName("Emotions")            # 識別子（無くても良い）
        action.triggered.connect(self.print_happy)  # ボタンを押したら呼び出す関数
        menuList.addAction(action)                  # 喜の機能をメニューに追加

        # 怒りのメニューとその機能を追加
        action = QtWidgets.QAction("怒", menuList)
        action.setObjectName("Emotions")
        action.triggered.connect(self.print_angry)
        menuList.addAction(action)

        # 哀しみのメニューとその機能を追加
        action = QtWidgets.QAction("哀", menuList)
        action.setObjectName("Emotions")
        action.triggered.connect(self.print_sad)
        menuList.addAction(action)

        # 楽しみのメニューとその機能を追加
        action = QtWidgets.QAction("楽", menuList)
        action.setObjectName("Emotions")
        action.triggered.connect(self.print_pleasant)
        menuList.addAction(action)

        # メニューボタンを定義
        menu_button = QtWidgets.QPushButton("喜怒哀楽を表現", self)
        menu_button.setMenu(menuList)  # ボタンに上記に定義した全メニューを登録

    # 喜び
    def print_happy(self):
        print("ヾ(*´∀`*)ﾉ")

    # 怒り
    def print_angry(self):
        print("（#＾ω＾）ﾋﾟｷﾋﾟｷ")

    # 哀しみ
    def print_sad(self):
        print("（´・ω・`）ｼｮﾎﾞｰﾝ")

    # 楽しみ
    def print_pleasant(self):
        print("(≧∇≦)")



# アプリの実行と終了
app = QtWidgets.QApplication()
window = MainWindow()
window.show()
app.exec_()
