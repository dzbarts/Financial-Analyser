# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myApp.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QAbstractTableModel, QVariant
from PyQt5.QtWidgets import QDesktopWidget, QHeaderView, QMessageBox

from parse import parsing_RBC, parsing_moex, parsing_invest_funds
from Sectors import tsectors, t_port_sect
from Countries import tcapa, t_port_capa


def main():
    sizeObject = QDesktopWidget().screenGeometry(-1)  # -1 означает, что мы берем на измерение текущий экран
    heignt = sizeObject.height()
    width = sizeObject.width()
    return [int(heignt), int(width)]


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(main()[1], main()[0])
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, main()[1], main()[0]))
        self.tabWidget.setIconSize(QtCore.QSize(50, 20))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.comboBox = QtWidgets.QComboBox(self.tab_1)
        self.comboBox.setGeometry(QtCore.QRect(20, 20, 181, 41))
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.tab_2)
        self.stackedWidget.setGeometry(QtCore.QRect(-10, 0, main()[1], main()[0]))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.comboBox_NEWS = QtWidgets.QComboBox(self.page_1)
        self.comboBox_NEWS.setGeometry(QtCore.QRect(20, 20, 171, 41))
        self.comboBox_NEWS.setObjectName("comboBox_NEWS")
        self.comboBox_NEWS.addItem("")
        self.comboBox_NEWS.addItem("")
        self.comboBox_NEWS.addItem("")
        self.renew_btn_NEWS = QtWidgets.QPushButton(self.page_1)
        self.renew_btn_NEWS.setGeometry(QtCore.QRect(720, 20, 141, 31))
        self.renew_btn_NEWS.setObjectName("renew_btn_NEWS")
        self.NEWS_label = QtWidgets.QLabel(self.page_1)
        self.NEWS_label.setGeometry(QtCore.QRect(20, 70, 271, 41))
        self.NEWS_label.setObjectName("NEWS_label")
        self.news_NEWS = QtWidgets.QTextBrowser(self.page_1)
        self.news_NEWS.setGeometry(QtCore.QRect(20, 110, main()[1] - 30, main()[0] - 350))
        self.news_NEWS.setObjectName("news_NEWS")
        self.stackedWidget.addWidget(self.page_1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.column_names = ['Ранняя фаза', 'Средняя фаза', 'Закат', 'Рецессия']
        self.view = QtWidgets.QTableView(self.tab_3)
        self.view.setGeometry(QtCore.QRect(50, 50, 1200, 328))
        self.view.setObjectName("table_data")
        self.model = PandasModel(tsectors, headers_column=['Ранняя фаза', 'Средняя фаза', 'Закат', 'Рецессия'],
                                 headers_row=['1', '2', '3', '4', '5', '6', '', 'Рекомендации'])
        self.view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.view.setModel(self.model)
        self.view_2 = QtWidgets.QTableView(self.tab_3)
        self.view_2.setGeometry(QtCore.QRect(50, 400, 700, 400))
        self.view_2.setObjectName("table_data")
        self.model_2 = PandasModel(tcapa, headers_column=['Country', 'Calculated Using', 'Index'],
                                   headers_row=[str(i) for i in range(1, tcapa.shape[0] + 1)])
        self.view_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.view_2.setModel(self.model_2)
        self.view_3 = QtWidgets.QTableView(self.tab_3)
        self.view_3.setGeometry(QtCore.QRect(770, 400, 480, 254))
        self.view_3.setObjectName("table_data")
        self.model_3 = PandasModel(t_port_sect, headers_column=['Stocks', 'Number', 'Sectors'],
                                   headers_row=[str(i) for i in range(1, t_port_sect.shape[0] + 1)])
        self.view_3.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.view_3.setModel(self.model_3)
        self.view_4 = QtWidgets.QTableView(self.tab_3)
        self.view_4.setGeometry(QtCore.QRect(770, 690, 480, 254))
        self.view_4.setObjectName("table_data")
        self.model_4 = PandasModel(t_port_capa, headers_column=['Stocks', 'Number', 'Countries'],
                                   headers_row=[str(i) for i in range(1, t_port_capa.shape[0] + 1)])
        self.view_4.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.view_4.setModel(self.model_4)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.edit = QtWidgets.QTextEdit(self.tab_4)
        self.edit.setGeometry(QtCore.QRect(20, 20, 150, 31))
        self.edit.setObjectName("editable")
        self.add_btn = QtWidgets.QPushButton(self.tab_4)
        self.add_btn.setGeometry(QtCore.QRect(720, 20, 180, 31))
        self.add_btn.setObjectName("add_btn")
        self.add_btn.setText("Add stock into the portfolio")
        self.remove_btn = QtWidgets.QPushButton(self.tab_4)
        self.remove_btn.setGeometry(QtCore.QRect(920, 20, 250, 31))
        self.remove_btn.setObjectName("remove_btn")
        self.remove_btn.setText("Remove the stock from the portfolio")
        self.clear_all_btn = QtWidgets.QPushButton(self.tab_4)
        self.clear_all_btn.setGeometry(QtCore.QRect(1500, 20, 150, 31))
        self.clear_all_btn.setObjectName("clear_btn")
        self.clear_all_btn.setText("Clear the portfolio")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.comboBox_5 = QtWidgets.QComboBox(self.tab_5)
        self.comboBox_5.setGeometry(QtCore.QRect(20, 20, 181, 41))
        self.comboBox_5.setEditable(True)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.comboBox_6 = QtWidgets.QComboBox(self.tab_6)
        self.comboBox_6.setGeometry(QtCore.QRect(20, 20, 181, 41))
        self.comboBox_6.setEditable(True)
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.comboBox_7 = QtWidgets.QComboBox(self.tab_7)
        self.comboBox_7.setGeometry(QtCore.QRect(20, 20, 181, 41))
        self.comboBox_7.setEditable(True)
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.tabWidget.addTab(self.tab_7, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.news_NEWS.setText(parsing_RBC())
        self.renew_btn_NEWS.clicked.connect(self.path_to_the_page)
        self.news_NEWS.setOpenExternalLinks(True)
        self.add_btn.clicked.connect(self.add_to_the_portfolio)
        self.remove_btn.clicked.connect(self.remove_the_stock)
        self.clear_all_btn.clicked.connect(self.clear_all)

    def rewrite_port(self, str):
        with open('proj.txt', 'a') as txt:
            txt.write(str + '\n')

    def remove_from_port(self, str):
        with open("proj.txt", "r") as f:
            lines = f.readlines()
        with open("proj.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != str:
                    f.write(line)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "New Item 1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "New Item 2"))
        self.comboBox.setItemText(2, _translate("MainWindow", "New Item 3"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Page 1"))
        self.comboBox_NEWS.setItemText(0, _translate("MainWindow", "RBC"))
        self.comboBox_NEWS.setItemText(1, _translate("MainWindow", "Invest Funds: Today News"))
        self.comboBox_NEWS.setItemText(2, _translate("MainWindow", "MOEX"))
        self.renew_btn_NEWS.setText(_translate("MainWindow", "RENEW"))
        self.NEWS_label.setText(_translate("MainWindow", "RBC"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Page 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Page 3"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Page 4"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "New Item 1"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "New Item 2"))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "New Item 3"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Page 5"))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "New Item 1"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "New Item 2"))
        self.comboBox_6.setItemText(2, _translate("MainWindow", "New Item 3"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Page 6"))
        self.comboBox_7.setItemText(0, _translate("MainWindow", "New Item 1"))
        self.comboBox_7.setItemText(1, _translate("MainWindow", "New Item 2"))
        self.comboBox_7.setItemText(2, _translate("MainWindow", "New Item 3"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "Page 7"))

    def path_to_the_page(self):
        if self.comboBox_NEWS.currentText() == 'RBC':
            self.NEWS_label.setText('RBS')
            self.news_NEWS.setText(parsing_RBC())
        elif self.comboBox_NEWS.currentText() == 'Invest Funds: Today News':
            self.NEWS_label.setText('Invest Funds: Today News')
            self.news_NEWS.setText(parsing_invest_funds())
            if len(parsing_invest_funds()) == 0:
                self.news_NEWS.setText("News can't be founded today. Go to sleep and wait for it!")
        elif self.comboBox_NEWS.currentText() == 'MOEX':
            self.NEWS_label.setText('MOEX')
            self.news_NEWS.setText(parsing_moex())

    def add_to_the_portfolio(self):
        if self.edit.toPlainText() == '':
            error = QMessageBox()
            error.setWindowTitle("Ошибка набора")
            error.setText("Пустой текст")
            error.setIcon(QMessageBox.Warning)
            error.exec_()
        else:
            self.rewrite_port(self.edit.toPlainText())
            self.edit.clear()

    def remove_the_stock(self):
        if self.edit.toPlainText() == '':
            error = QMessageBox()
            error.setWindowTitle("Ошибка набора")
            error.setText("Пустой текст")
            error.setIcon(QMessageBox.Warning)
            error.exec_()
        else:
            self.remove_from_port(self.edit.toPlainText())
            self.edit.clear()

    def clear_all(self):
        with open('proj.txt', 'w'):
            pass


class PandasModel(QAbstractTableModel):
    def __init__(self, data, headers_row, headers_column, parent=None):
        QAbstractTableModel.__init__(self, parent)
        self.data = data
        self.headers_row = headers_row
        self.headers_column = headers_column

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:  # Проверяем есть ли ячейка для отображения данных
            if orientation == QtCore.Qt.Horizontal:  # Если это загловки  столбцов
                return self.headers_column[section]  # То задаем соответствующее значение заголовков по индексу
            else:  # Иначе  это заголовки строк
                if not self.headers_row:
                    return section + 1
                return self.headers_row[section]  # То задаем соответствующее значение заголовков по индексу

    def rowCount(self, parent=None):
        return len(self.data.values)

    def columnCount(self, parent=None):
        return self.data.columns.size

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if index.isValid():
            if role == QtCore.Qt.DisplayRole:
                return QVariant(str(self.data.iloc[index.row()][index.column()]))
        return QVariant()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
