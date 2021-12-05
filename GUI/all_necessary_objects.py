from PyQt5 import QtWidgets,QtCore
from canvas import GraphicsCanvas
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar

class label(QtWidgets.QLabel):
    def __init__(self, text, geometry):
        super(label, self).__init__()
        self.setText(text)
        self.setGeometry(geometry)


class combobox(QtWidgets.QComboBox):
    def __init__(self, items, geometry):
        super(combobox, self).__init__()
        self.addItems(items)
        self.setGeometry(geometry)


class table_view(QtWidgets.QTableView):
    def __init__(self, model, geometry):
        super(table_view, self).__init__()
        self.setModel(model)
        self.setGeometry(geometry)


class push_button(QtWidgets.QPushButton):
    def __init__(self, text, geometry):
        super(push_button, self).__init__()
        self.setText(text)
        self.setGeometry(geometry)


