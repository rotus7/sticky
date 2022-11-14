import subprocess
# PySide2のモジュールを読み込む
from PySide2 import QtWidgets


# ウィンドウの見た目と各機能
class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 500, 150)

        # アプリの案内を表示
        label = QtWidgets.QLabel(self)
        label.setStyleSheet("""QLabel {
            font-size: 24px;        /* 文字サイズ */
            font-weight: bold;      /* 太文字 */
            font-family: umeboshi;  /* 梅干フォント */
        }""")
        label.setText("起動したいアプリを選択してください：")

        # ラジオボタンのグループ登録用オブジェクト
        self.radioGroup = QtWidgets.QButtonGroup()

        # ラジオボタンオブジェクトの生成
        chromeButton = QtWidgets.QRadioButton("Chrome", self)
        sakuraButton = QtWidgets.QRadioButton("サクラエディタ", self)
        kindleButton = QtWidgets.QRadioButton("Kindle", self)

        # ラジオボタンオブジェクトのグループ登録
        self.radioGroup.addButton(chromeButton, 1)
        self.radioGroup.addButton(sakuraButton, 2)
        self.radioGroup.addButton(kindleButton, 3)

        # Chromeを初期入力として設定
        chromeButton.setChecked(True)

        # ラジオボタンの配置設定
        chromeButton.move(10, 30)
        sakuraButton.move(10, 60)
        kindleButton.move(10, 90)

        # 起動ボタン
        runButton = QtWidgets.QPushButton("アプリを起動", self)
        runButton.clicked.connect(self.run_application)
        runButton.move(10, 120)

    def run_application(self):
        appId = {
            "Chrome": 1,
            "Sakura": 2,
            "Kindle": 3
        }

        if appId["Chrome"] == self.radioGroup.checkedId():
            subprocess.Popen(R"C:\Program Files\Google\Chrome\Application\chrome.exe")
        elif appId["Sakura"] == self.radioGroup.checkedId():
            subprocess.Popen(R"C:\Program Files (x86)\sakura\sakura.exe")
        elif appId["Kindle"] == self.radioGroup.checkedId():
            subprocess.Popen(R"C:\Users\からくり\AppData\Local\Amazon\Kindle\application\Kindle.exe")
        else:
            print("Unknown")


# アプリの実行と終了
app = QtWidgets.QApplication()
window = MainWindow()
window.show()
app.exec_()
