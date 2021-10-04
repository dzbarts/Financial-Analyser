import sys
from PyQt5 import QtCore, QtWidgets
from Table import *


class PandasModel(QtCore.QAbstractTableModel):
    def __init__(self, data, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data.values)

    def columnCount(self, parent=None):
        return self._data.columns.size

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if index.isValid():
            if role == QtCore.Qt.DisplayRole:
                return QtCore.QVariant(str(
                    self._data.iloc[index.row()][index.column()]))
        return QtCore.QVariant()


if __name__ == '__main__':
    application = QtWidgets.QApplication(sys.argv)
    view = QtWidgets.QTableView()
    model = PandasModel(tsectors)
    view.setModel(model)
    view.show()
    sys.exit(application.exec_())
