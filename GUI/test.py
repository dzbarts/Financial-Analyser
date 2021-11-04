from PyQt5 import QtGui, QtCore,QtWidgets
import sys


class Window(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        layout = QtWidgets.QVBoxLayout(self)
        self.combo = QtWidgets.QComboBox()
        self.combo.setEditable(True)
        self.combo.addItems('One Two Three Four Five'.split())
        self.buttonOne = QtWidgets.QPushButton('Change (Default)', self)
        self.buttonOne.clicked.connect(self.handleButtonOne)
        self.buttonTwo = QtWidgets.QPushButton('Change (Blocked)', self)
        self.buttonTwo.clicked.connect(self.handleButtonTwo)
        layout.addWidget(self.combo)
        layout.addWidget(self.buttonOne)
        layout.addWidget(self.buttonTwo)
        self.changeIndex()
        self.combo.activated['QString'].connect(self.handleActivated)
        self.combo.currentIndexChanged['QString'].connect(self.handleChanged)
        self.changeIndex()

    def handleButtonOne(self):
        self.changeIndex()

    def handleButtonTwo(self):
        self.combo.blockSignals(True)
        self.changeIndex()
        self.combo.blockSignals(False)

    def changeIndex(self):
        index = self.combo.currentIndex()
        if index < self.combo.count() - 1:
            self.combo.setCurrentIndex(index + 1)
        else:
            self.combo.setCurrentIndex(0)

    def handleActivated(self, text):
        print('handleActivated: %s' % text)

    def handleChanged(self, text):
        print('handleChanged: %s' % text)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())