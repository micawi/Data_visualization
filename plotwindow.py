from PyQt5.QtWidgets import QWidget;
from PyQt5.QtGui import QFont;
from math import log10;
import matplotlib.pyplot as plot;

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
        self.XSize = 600;
        self.YSize = 600;
        
        self.setFixedSize(self.XSize, self.YSize);
        self.setWindowTitle(plotType);

        if(yDataManually == False):
            self.YDataValues = [];
            with open(yFilePath, "r") as f:
                for line in f:
                    self.YDataValues.append(float(line));
        if(xDataManually == False):
            if((plotType == "Standard Plot") | (plotType == "Logarithmic Plot")):
                self.XDataValues = [];
                with open(xFilePath, "r") as f:
                    for line in f:
                        self.XDataValues.append(float(line));
            else:
                with open(xFilePath, "r") as f:
                    self.XDataValues = int(f.read());
        
        if(plotType == "Logarithmic Plot"):
            for i in range(0, len(self.YDataValues)):
                self.YDataValues[i] = log10(self.YDataValues[i]);
    
        if(plotType == "Standard Plot"):
            plot.plot(self.XDataValues, self.YDataValues);
            plot.ylabel("Value of y");
            plot.xlabel("Value of x");
            plot.title("Standard plot");
        elif(plotType == "Logarithmic Plot"):
            plot.plot(self.XDataValues, self.YDataValues);
            plot.ylabel("Value of log10(y)");
            plot.xlabel("Value of x");   
            plot.title("Logarithmic plot"); 
        else:
            plot.hist(self.YDataValues, self.XDataValues);
            plot.ylabel("Quantity of y-values in bins");
            plot.xlabel("Value of y");
            plot.title("Histogram");
        
        plot.show();
