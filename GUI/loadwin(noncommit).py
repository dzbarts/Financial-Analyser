# -*- coding: utf-8 -*-
import sys
from PyQt5.QtCore import Qt, QSize, pyqtSignal
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QWidget, QSizePolicy, QVBoxLayout, QProgressBar, QLabel, QMainWindow, QApplication
import time


class loading_window(QWidget):
    def __init__(self, parrent = None):
        """
        тут ваще ничего интересного обычное обьявлялово виджетов, см след коммент
        """
        QWidget.__init__(self, parrent)
        self.click_count = 0
        self.current_loading = 5
        self.setObjectName("loading")
        self.resize(400, 200)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy1)
        self.setMinimumSize(QSize(400, 200))
        self.setMaximumSize(QSize(400, 200))
        self.setCursor(QCursor(Qt.WaitCursor))
        self.setContextMenuPolicy(Qt.NoContextMenu)
        self.setStyleSheet("background-color: rgb(0, 0, 0);\n border-color: rgb(0, 0, 0);\n alternate-background-color: rgb(0, 0, 0);")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.setLayout(self.verticalLayout)
        self.progressBar = QProgressBar(self)
        self.progressBar.setProperty("value", self.current_loading)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setFixedHeight(10)
        self.progressBar.setFixedWidth(380)
        self.progressBar.setTextVisible(False)
        self.verticalLayout.addWidget(self.progressBar, Qt.AlignBottom|Qt.AlignLeft)
        self.label = QLabel(self)
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setCursor(QCursor(Qt.WaitCursor))
        self.label.setContextMenuPolicy(Qt.NoContextMenu)
        self.label.setStyleSheet("color: rgb(170, 170, 255);")
        self.label.setTextInteractionFlags(Qt.NoTextInteraction)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, Qt.AlignBottom|Qt.AlignLeft)
        self.verticalLayout.setAlignment(self.progressBar, Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.label.setText("loading...")
        self.show()
    def update_progress_bar(self, val):
        curval = self.progressBar.property('value')
        while curval < val:
            curval +=1
            self.progressBar.setProperty('value' , curval)
            time.sleep(0.1)
            QApplication.processEvents()

class acc(QMainWindow):
    loaded = pyqtSignal(int)
    def __init__(self, loader , parrent = None):
        self.loader = loader
        QMainWindow.__init__(self, parrent)
        """
        перенес всю инициализацию в метод linit, для того что-бы перед инициализацией всего дерьма
        иметь возможность поместить сюда ссылки на объекты классов loading_window, QApplication и прочих
        а так-же вести инициализацию из другого потока
        """
    def linit(self):
        self.loaded.emit(1)
        time.sleep(2)
        print('import modules')
        self.loaded.emit(20)
        time.sleep(5)
        print('load GUI')
        self.loaded.emit(40)
        time.sleep(5)
        print('import data')
        self.loaded.emit(60)
        time.sleep(3)
        print('other shit')
        self.loaded.emit(100)
        self.show()
        self.loader.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    loader = loading_window() #создаем окно прогреса заргузки
    wnd = acc(loader) # создаем основное окно
    wnd.loaded.connect(loader.update_progress_bar) # соединяем сигналом
    wnd.linit() #запускаем инициализацию главного окна.
    sys.exit(app.exec_())