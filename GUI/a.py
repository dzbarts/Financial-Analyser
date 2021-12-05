from PyQt5.QtCore import Qt, QSize, pyqtSignal
from PyQt5.QtGui import QCursor, QMovie
from PyQt5.QtWidgets import QWidget, QSizePolicy, QVBoxLayout, QProgressBar, QLabel, QMainWindow, QApplication
import time

from all_necessary_objects import *
from pandasmodel import PandasModel
import pandas as pd
import numpy as np


class MyWindow(QMainWindow):
    loaded = pyqtSignal(int)

    def __init__(self, loader, parrent=None):
        self.loader = loader
        QMainWindow.__init__(self, parrent)

    def setUpUI(self, MyWindow):
        import time
        self.loaded.emit(1)
        MyWindow.setFixedSize(500, 500)
        self.centralwidget = QtWidgets.QWidget(MyWindow)
        self.tabwidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tab = QtWidgets.QWidget()
        time.sleep(3)
        print('main')
        self.loaded.emit(20)
        self.label = label('Hi world', QtCore.QRect(400, 300, 200, 50))
        self.btnQuit = push_button('Close window', QtCore.QRect(400, 400, 200, 50))
        d2 = {"p": np.array([1, 2, 3]),
              "c": np.array([10, 12, 7])}
        self.stock_growth = pd.DataFrame(d2, index=['v1', 'v2', 'v3'])
        self.table = table_view(PandasModel(self.stock_growth, headers_column=['price', 'count'],
                                            headers_row=[str(i) for i in
                                                         range(1, self.stock_growth.shape[0] + 1)]), QtCore.QRect(400, 500, 500, 254))
        time.sleep(5)
        print('widgets')
        self.loaded.emit(60)
        self.btnQuit.clicked.connect(QtWidgets.qApp.quit)
        self.layout = QtWidgets.QVBoxLayout(self.tab)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.btnQuit)
        self.layout.addWidget(self.table)
        time.sleep(3)
        print('adding')
        self.tabwidget.addTab(self.tab, "Page 1")

        MyWindow.setCentralWidget(self.centralwidget)
        time.sleep(3)
        self.loaded.emit(100)
        self.loader.close()


class loading_window(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.click_count = 0
        self.current_loading = 5
        self.setFixedSize(400, 200)
        self.setCursor(QCursor(Qt.WaitCursor))
        self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setStyleSheet("background-color: rgb(0, 0, 0);\n border-color: rgb(0, 0, 0);")
        self.verticalLayout = QVBoxLayout()
        self.setLayout(self.verticalLayout)
        self.progressBar = QProgressBar(self)
        self.progressBar.setProperty("value", self.current_loading)
        self.progressBar.setFixedSize(380, 10)
        self.progressBar.setTextVisible(False)
        self.verticalLayout.addWidget(self.progressBar, Qt.AlignBottom | Qt.AlignLeft)
        self.label = QLabel(self)
        sizePolicy2 = QSizePolicy()
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setCursor(QCursor(Qt.WaitCursor))
        self.label.setText("loading...")
        self.label.setStyleSheet("color: rgb(170, 170, 255);")
        self.label_for_gif = QLabel()
        self.gif = QMovie("animated-web-preloader.gif")
        self.label_for_gif.setMovie(self.gif)
        self.gif.start()
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout.addWidget(self.label_for_gif)
        self.verticalLayout.setAlignment(self.progressBar, Qt.AlignBottom | Qt.AlignLeft)
        self.label.setText("loading...")
        self.show()

    def update_progress_bar(self, val):
        progress_bar = self.progressBar.property('value')
        while progress_bar < val:
            progress_bar += 1
            self.progressBar.setProperty('value', progress_bar)
            time.sleep(0.1)
            QApplication.processEvents()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    loader = loading_window()  # создаем окно прогресса загрузки
    MainWindow = QtWidgets.QMainWindow()
    window = MyWindow(loader)
    window.loaded.connect(loader.update_progress_bar)  # соединяем сигналом
    window.setUpUI(MainWindow)
    MainWindow.show()  # Отображаем окно
    sys.exit(app.exec_())  # Запускаем цикл обработки событий
