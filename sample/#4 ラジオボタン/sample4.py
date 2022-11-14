import multiprocessing
import psutil
# PySide2のモジュールを読み込む
from PySide2 import QtWidgets


# ウィンドウの見た目と各機能
class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 600, 300)

        # アプリの案内を表示
        label = QtWidgets.QLabel(self)
        label.setStyleSheet("""QLabel {
            font-size: 24px;        /* 文字サイズ */
            font-weight: bold;      /* 太字 */
        }""")
        label.setText("確認したいリソース情報を選択してください：")

        # ラジオボタンのグループ登録用オブジェクト
        self.radioGroup = QtWidgets.QButtonGroup()

        # ラジオボタンオブジェクトの生成
        cpuCore = QtWidgets.QRadioButton("CPUコア数", self)
        cpuUseRate = QtWidgets.QRadioButton("CPU使用率", self)
        ramCapacity = QtWidgets.QRadioButton("メモリ容量", self)
        ramUseRate = QtWidgets.QRadioButton("メモリ使用率", self)
        storageCapacity = QtWidgets.QRadioButton("ストレージ容量", self)
        storageUseRate = QtWidgets.QRadioButton("ストレージ使用率", self)
        storageFreeSpace = QtWidgets.QRadioButton("ストレージ空き容量", self)

        # ラジオボタンオブジェクトのグループ登録
        self.radioGroup.addButton(cpuCore,          1)
        self.radioGroup.addButton(cpuUseRate,       2)
        self.radioGroup.addButton(ramCapacity,      3)
        self.radioGroup.addButton(ramUseRate,       4)
        self.radioGroup.addButton(storageCapacity,  5)
        self.radioGroup.addButton(storageUseRate,   6)
        self.radioGroup.addButton(storageFreeSpace, 7)

        # CPUコア数を初期入力として設定
        cpuCore.setChecked(True)

        # ラジオボタンの配置設定
        cpuCore.move(10, 30)
        cpuUseRate.move(10, 60)
        ramCapacity.move(10, 90)
        ramUseRate.move(10, 120)
        storageCapacity.move(10, 150)
        storageUseRate.move(10, 180)
        storageFreeSpace.move(10, 210)

        # 表示ボタン
        showButton = QtWidgets.QPushButton("リソース情報表示", self)
        showButton.clicked.connect(self.get_pc_resource)
        showButton.move(10, 240)

    def get_pc_resource(self):
        resourceId = {
            "cpu_core":             1,  # CPUコア数
            "cpu_use_rate":         2,  # CPU使用率
            "ram_capacity":         3,  # メモリ容量
            "ram_use_rate":         4,  # メモリ使用率
            "storage_capacity":     5,  # ストレージ容量
            "storage_use_rate":     6,  # ストレージ使用率
            "storage_free_space":   7   # ストレージ空き容量
        }

        # メモリ情報の取得
        ram = psutil.virtual_memory()

        # ストレージ情報の取得
        storage = psutil.disk_usage("/")

        # リソース情報を表示
        if resourceId["cpu_core"] == self.radioGroup.checkedId():
            print("CPUコア数:", multiprocessing.cpu_count())
        elif resourceId["cpu_use_rate"] == self.radioGroup.checkedId():
            print("CPU使用率:", psutil.cpu_percent(interval=1))
        elif resourceId["ram_capacity"] == self.radioGroup.checkedId():
            print("メモリ容量:", ram.total)
        elif resourceId["ram_use_rate"] == self.radioGroup.checkedId():
            print("メモリ使用率:", ram.used)
        elif resourceId["storage_capacity"] == self.radioGroup.checkedId():
            print("ストレージ容量:", storage.total)
        elif resourceId["storage_use_rate"] == self.radioGroup.checkedId():
            print("ストレージ使用率:", storage.used)
        elif resourceId["storage_free_space"] == self.radioGroup.checkedId():
            print("ストレージ空き容量:", storage.free)
        else:
            print("Unknown")


# アプリの実行と終了
app = QtWidgets.QApplication()
window = MainWindow()
window.show()
app.exec_()
