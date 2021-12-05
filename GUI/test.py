from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.pbar = QProgressBar(self)
        self.percentage = 0
        self.pbar.setTextVisible(self.percentage)
        self.pbar.setValue(self.percentage)

        button = QPushButton("Старт ProgressBar")
        button.clicked.connect(self.onClicked)

        self.gridLayout = QGridLayout(self)
        self.gridLayout.addWidget(self.pbar)
        self.gridLayout.addWidget(button)

    def onClicked(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.ProgressBar)
        self.timer.start(500)

    def ProgressBar(self):
        self.pbar.setValue(self.percentage)
        self.pbar.setTextVisible(self.percentage)
        if self.percentage >= 100:
            self.timer.stop()
            self.percentage = 0
        else:
            self.percentage += 5


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = Widget()
    w.setGeometry(400, 300, 300, 150)
    w.setWindowTitle('Demo ProgressBar')
    w.show()
    sys.exit(app.exec())