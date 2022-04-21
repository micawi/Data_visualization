from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton, QLineEdit, QComboBox, QFrame;
from PyQt5.QtGui import QFont;

appVersion: str = "v.1.0";

class MainWindow(QWidget):
    # Size properties
    XSize: int;
    YSize: int;

    # Layout properties
    Grid: QGridLayout;
    HLine0: QFrame;
    HLine1: QFrame;
    HLine2: QFrame;

    # Elements
    PlotTypeLbl: QLabel;
    PlotTypeBox: QComboBox;
    PlotTypeOkBtn: QPushButton;
    SelectYLbl: QLabel;
    SelectYBox: QComboBox;
    OkYBtn: QPushButton;
    YDataLine: QLineEdit;
    LoadedYFileLbl: QLabel;
    SelectXLbl: QLabel;
    SelectXBox: QComboBox;
    OkXBtn: QPushButton;
    XDataLine: QLineEdit;
    LoadedXFileLbl: QLabel;
    XBinsLine: QLineEdit;
    PlotBtn: QPushButton;

    def __init__(self):
        # Window initialization with params
        super().__init__();
        self.XSize = 500; 
        self.YSize = 500;
        self.setFixedSize(self.XSize, self.YSize);
        self.setWindowTitle("Data visualizer " + appVersion);
        self.setFont(QFont("Arial", 10));

        # Layout initialization
        self.Grid = QGridLayout(self);

        self.HLine0 = QFrame();
        self.HLine0.setFrameShape(QFrame.HLine);
        self.Grid.addWidget(self.HLine0, 1, 0, 1, 4);

        self.HLine1 = QFrame();
        self.HLine1.setFrameShape(QFrame.HLine);
        self.Grid.addWidget(self.HLine1, 4, 0, 1, 4);

        self.HLine2 = QFrame();
        self.HLine2.setFrameShape(QFrame.HLine);
        self.Grid.addWidget(self.HLine2, 7, 0, 1, 4);

        # Elements initialization
        self.PlotTypeLbl = QLabel();
        self.PlotTypeLbl.setText("Select visualization method: ");
        self.Grid.addWidget(self.PlotTypeLbl, 0, 0);

        self.PlotTypeBox = QComboBox();
        self.PlotTypeBox.addItem("Standard Plot");
        self.PlotTypeBox.addItem("Logarithmic Plot");
        self.PlotTypeBox.addItem("Histogram");
        self.Grid.addWidget(self.PlotTypeBox, 0, 1);

        self.PlotTypeOkBtn = QPushButton("OK");
        self.Grid.addWidget(self.PlotTypeOkBtn, 0, 2);

        self.SelectYLbl = QLabel();
        self.SelectYLbl.setText("Select y-data insertion method: ");
        self.Grid.addWidget(self.SelectYLbl, 2, 0);

        self.SelectYBox = QComboBox();
        self.SelectYBox.addItem("Insert x-data manually");
        self.SelectYBox.addItem("Load data from file");
        self.Grid.addWidget(self.SelectYBox, 2, 1);

        self.OkYBtn = QPushButton("OK");
        self.Grid.addWidget(self.OkYBtn, 2, 2);

        self.YDataLine = QLineEdit();
        self.YDataLine.setPlaceholderText("Type array here...");
        self.Grid.addWidget(self.YDataLine, 3, 0, 1, 4);

        self.LoadedYFileLbl = QLabel();
        self.Grid.addWidget(self.LoadedYFileLbl, 3, 0);
        self.LoadedYFileLbl.hide();

        self.SelectXLbl = QLabel();
        self.SelectXLbl.setText("Select x-data insertion method: ");
        self.Grid.addWidget(self.SelectXLbl, 5, 0);

        self.SelectXBox = QComboBox();
        self.SelectXBox.addItem("Insert data manually");
        self.SelectXBox.addItem("Load data from file");
        self.Grid.addWidget(self.SelectXBox, 5, 1);

        self.OkXBtn = QPushButton("OK");
        self.Grid.addWidget(self.OkXBtn, 5, 2);

        self.XDataLine = QLineEdit();
        self.XDataLine.setPlaceholderText("Type array here...");
        self.Grid.addWidget(self.XDataLine, 6, 0, 1, 4);

        self.LoadedXFileLbl = QLabel();
        self.Grid.addWidget(self.LoadedXFileLbl, 6, 0);
        self.LoadedXFileLbl.hide();

        self.XBinsLine = QLineEdit();
        self.XBinsLine.setPlaceholderText("Type bin separation interval here...");
        self.Grid.addWidget(self.XBinsLine, 6, 0);
        self.XBinsLine.hide();

        self.PlotBtn = QPushButton("PLOT DATA");
        self.PlotBtn.setFixedHeight(50);
        self.Grid.addWidget(self.PlotBtn, 8, 0, 1, 4);

        self.show();