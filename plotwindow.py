from PyQt5.QtWidgets import QWidget;
from PyQt5.QtGui import QFont;
from matplotlib.pyplot import plot, hist;

class PlotWindow(QWidget):
    # Properties
    PlotType: str;
    YDataManually: bool;
    XDataManually: bool;
    YFilePath: str;
    XFilePath: str;
    YDataValues: list;
    XDataValues: any;

    # Size properties
    XSize: int;
    YSize: int;

    # Initialization
    def __init__(self, plotType: str, yDataManually: bool, xDataManually: bool, yFilePath: str, xFilePath: str, 
    yDataValues: list, xDataValues: any):
        super().__init__();
        self.PlotType = plotType;
        self.YDataManually = yDataManually;
        self.XDataManually = xDataManually;
        self.YFilePath = yFilePath;
        self.XFilePath = xFilePath;
        self.YDataValues = yDataValues;
        self.XDataValues = xDataValues;
        self.XSize = 1000;
        self.YSize = 1000;
        
        self.setFixedSize(self.XSize, self.YSize);
        self.setWindowTitle(plotType);

        self.show();
