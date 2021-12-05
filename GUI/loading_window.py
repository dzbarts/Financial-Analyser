from PyQt5.QtGui import QCursor, QMovie
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QProgressBar, QLabel, QSizePolicy, QApplication, QMainWindow
from PyQt5.QtCore import Qt


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
        self.show()

    def update_progress_bar(self, val):
        import time
        progress_bar = self.progressBar.property('value')
        while progress_bar < val:
            progress_bar += 1
            self.progressBar.setProperty('value', progress_bar)
            time.sleep(0.1)
            QApplication.processEvents()