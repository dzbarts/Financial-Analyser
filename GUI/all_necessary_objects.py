from PyQt5 import QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QVBoxLayout, QLabel


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
                    font-weight: bold;
                    border: 1px solid #1DA1F2;
                    border-radius: 4px;
                    color: #1DA1F2;
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
