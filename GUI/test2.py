import time

from PyQt5 import QtGui, QtWidgets


class MyWindow(QtWidgets.QPushButton):
     def __init__(self):
         QtWidgets.QPushButton.__init__(self)
         self.setText("Закрыть окно")
         self.clicked.connect(QtWidgets.QApplication.quit)

     def load_data(self, sp):
         for i in range(1, 11):  # Имитируем процесс
             time.sleep(2)  # Что-то загружаем
             sp.showMessage("Загрузка данных... {0}%".format(i * 10))
             QtWidgets.QApplication.processEvents() # Запускаем оборот цикла


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    splash = QtWidgets.QSplashScreen(QtGui.QPixmap("Bez_imeni-3.png"))
    splash.showMessage("Загрузка данных... 0%")
    splash.show()  # Отображаем заставку
    QtWidgets.QApplication.processEvents()  # Запускаем оборот цикла
    window = MyWindow()
    window.setWindowTitle("Использование класса QSplashScreen")
    window.resize(300, 30)
    window.load_data(splash)  # Загружаем данные
    window.show()
    splash.finish(window)  # Скрываем заставку
    sys.exit(app.exec_())
