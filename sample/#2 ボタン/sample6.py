import subprocess
# PySide2のモジュールを読み込む
from PySide2 import QtWidgets


# ウィンドウの見た目と各機能（今はウィンドウだけ）
class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 300, 200)

        # メニューインスタンス生成
        menuList = QtWidgets.QMenu(self)

        # Chromeを起動するメニューとその機能を登録
        action = QtWidgets.QAction("Chromeを起動", menuList)
        action.setObjectName("run_applications")
        action.triggered.connect(self.run_chrome)
        menuList.addAction(action)

        # サクラエディタを起動するメニューとその機能を登録
        action = QtWidgets.QAction("サクラエディタを起動", menuList)
        action.setObjectName("run_applications")
        action.triggered.connect(self.run_sakura_editor)
        menuList.addAction(action)

        # Kindleを起動するメニューとその機能を登録
        action = QtWidgets.QAction("Kindleを起動", menuList)
        action.setObjectName("run_applications")
        action.triggered.connect(self.run_kindle)
        menuList.addAction(action)

        # 全部を起動するメニューとその機能を登録
        action = QtWidgets.QAction("全部を起動", menuList)
        action.setObjectName("run_applications")
        action.triggered.connect(self.run_all_applications)
        menuList.addAction(action)

        run_application_button = QtWidgets.QPushButton("何のアプリを起動する？", self)
        run_application_button.setMenu(menuList)

    def run_chrome(self):
        # エスケープシーケンスを無効にする「R」を忘れないで！！
        self.chromePath = R"C:\Program Files\Google\Chrome\Application\chrome.exe"
        subprocess.Popen(self.chromePath)

    def run_sakura_editor(self):
        # エスケープシーケンスを無効にする「R」を忘れないで！！
        self.sakuraeditorPath = R"C:\Program Files (x86)\sakura\sakura.exe"
        subprocess.Popen(self.sakuraeditorPath)

    def run_kindle(self):
        # エスケープシーケンスを無効にする「R」を忘れないで！！
        self.kindlePath = R"C:\Users\rotus\AppData\Local\Amazon\Kindle\application\Kindle.exe"
        subprocess.Popen(self.kindlePath)

    def run_all_applications(self):
        subprocess.Popen(self.chromePath)
        subprocess.Popen(self.sakuraeditorPath)
        subprocess.Popen(self.kindlePath)



# アプリの実行と終了
app = QtWidgets.QApplication()
window = MainWindow()
window.show()
app.exec_()
