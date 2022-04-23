from PyQt5.QtWidgets import QWidget;
from PyQt5.QtGui import QFont;

class PlotWindow(QWidget):
    # Properties
    PlotType: str;

    # Initialization
    def __init__(self, plotType: str):
        super().__init__();
