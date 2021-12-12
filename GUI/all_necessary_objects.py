from PyQt5 import QtWidgets,QtCore
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QVBoxLayout, QLabel

from canvas import GraphicsCanvas
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar


class label(QtWidgets.QLabel):
    def __init__(self, parent, text, geometry):
        super(label, self).__init__(parent)
        self.setText(text)
        self.setGeometry(geometry)


class combobox(QtWidgets.QComboBox):
    def __init__(self, parent, items, geometry):
        super(combobox, self).__init__(parent)
        self.addItems(items)
        self.setGeometry(geometry)


class table_view(QtWidgets.QTableView):
    def __init__(self, parent, model, geometry):
        super(table_view, self).__init__(parent)
        self.setModel(model)
        self.setGeometry(geometry)


class push_button(QtWidgets.QPushButton):
    def __init__(self, parent, text, geometry):
        super(push_button, self).__init__(parent)
        self.setText(text)
        self.setGeometry(geometry)


class dialog(QtWidgets.QDialog):
    def __init__(self):
        super(dialog, self).__init__()
        vbox = QVBoxLayout()
        lbl = QLabel()
        self.moviee = QMovie('a_giphy.gif')
        lbl.setMovie(self.moviee)
        self.moviee.start()
        vbox.addWidget(lbl)
        self.setLayout(vbox)
