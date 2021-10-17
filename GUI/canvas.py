from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class GraphicsCanvas(FigureCanvas):  # холст для помещения графика
    def __init__(self, fig, parent=None):
        self.fig = fig
        FigureCanvas.__init__(self, self.fig)  # в конструктор супепр-класса помещаем график
        FigureCanvas.setSizePolicy(self, QSizePolicy.Maximum, QSizePolicy.Expanding)  # график будет на всю область
        FigureCanvas.updateGeometry(self)
