from PyQt5 import QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QVBoxLayout, QLabel
from pandasmodel import PandasModel
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
    def __init__(self, parent, geometry, text):
        super(push_button, self).__init__(parent)
        self.setText(text)
        self.setGeometry(geometry)
        self.setStyleSheet("""
                QPushButton{
                    font-size: 15px;
                    font-weight: bold;
                    border: 1px solid #5AF2FF;
                    border-radius: 4px;
                    color: #5AF2FF;
                }
                """)


class dialog(QtWidgets.QDialog):
    def __init__(self):
        super(dialog, self).__init__()
        vbox = QVBoxLayout()
        lbl = QLabel()
        self.moviee = QMovie('necessary images and gifs/a_giphy.gif')
        lbl.setMovie(self.moviee)
        self.moviee.start()
        vbox.addWidget(lbl)
        self.setLayout(vbox)


class message_box(QtWidgets.QMessageBox):
    def __init__(self, title, text, icon, parent=None):
        super(message_box, self).__init__()
        self.setWindowTitle(title)
        self.setText(text)
        self.setIcon(icon)
        self.exec_()


class my_table_view(QtWidgets.QTableView):
    def __init__(self, parent, geometry, pandas_table, h_columns):
        super(my_table_view, self).__init__(parent)
        self.setGeometry(geometry)
        self.model = PandasModel(pandas_table, headers_column=h_columns,
                                 headers_row=[str(i) for i in range(1, pandas_table.shape[0] + 1)])
        self.setModel(self.model)


class my_plot_widget(QtWidgets.QWidget):
    def __init__(self, parent, geometry, fig, main_window):
        super(my_plot_widget, self).__init__(parent)
        self.setGeometry(geometry)
        self.fig = fig
        self.layout = QtWidgets.QVBoxLayout(self)
        self.canvas = GraphicsCanvas(self.fig)
        self.layout.addWidget(self.canvas)
        self.toolbar = NavigationToolbar(self.canvas, main_window)
        self.layout.addWidget(self.toolbar)
