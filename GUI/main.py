import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow


class Window(QMainWindow):
    def __init__(self):  # конструктор
        super(Window, self).__init__()  # вызываем конструктор из род.класса
        # self - обращение к самому классу Window
        self.setWindowTitle("Finansical Analysis: This will help u to earn some money")
        self.move(600, 200)
        self.setFixedSize(600, 300)

        self.btn_txt = QtWidgets.QLabel(self)  # будет объект, содержащий надпись(изнач. пустой)

        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(300, 150)
        self.btn.setText("Push me.")
        self.btn.setFixedWidth(200)
        self.btn.clicked.connect(self.command)

    def command(self):
        self.btn_txt.setText('Ow, u push me.')


def creation():
    app = QtWidgets.QApplication(sys.argv)  # передаем набор настроек, связанных с устройством, на кот. выполн. программа
    win = Window()

    win.show()
    sys.exit(app.exec_())  # передаем корректные пар-ры выхода из системы


if __name__ == "__main__":
    creation()
