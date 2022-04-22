from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton, QLineEdit, QComboBox, QFrame;
from PyQt5.QtGui import QFont;
from PyQt5.QtCore import Qt;

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
    UploadFileYBtn: QPushButton;
    SelectXLbl: QLabel;
    SelectXBox: QComboBox;
    OkXBtn: QPushButton;
    XDataLine: QLineEdit;
    LoadedXFileLbl: QLabel;
    UploadFileXBtn: QPushButton;
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
        self.PlotTypeOkBtn.clicked.connect(self.plotTypeBtnClicked);
        self.Grid.addWidget(self.PlotTypeOkBtn, 0, 2);

        self.SelectYLbl = QLabel();
        self.SelectYLbl.setText("Select y-data insertion method: ");
        self.Grid.addWidget(self.SelectYLbl, 2, 0);

        self.SelectYBox = QComboBox();
        self.SelectYBox.addItem("Insert data manually");
        self.SelectYBox.addItem("Load data from file");
        self.Grid.addWidget(self.SelectYBox, 2, 1);

        self.OkYBtn = QPushButton("OK");
        self.OkYBtn.clicked.connect(self.yOkBtnClicked);
        self.Grid.addWidget(self.OkYBtn, 2, 2);

        self.YDataLine = QLineEdit();
        self.YDataLine.setPlaceholderText("Type array here...");
        self.Grid.addWidget(self.YDataLine, 3, 0, 1, 4);

        self.LoadedYFileLbl = QLabel();
        self.LoadedYFileLbl.setText("No file loaded");
        self.LoadedYFileLbl.setFixedHeight(16);
        self.Grid.addWidget(self.LoadedYFileLbl, 3, 0);
        self.LoadedYFileLbl.hide();

        self.UploadFileYBtn = QPushButton("Upload file");
        self.UploadFileYBtn.setFixedHeight(22);
        self.Grid.addWidget(self.UploadFileYBtn, 3, 1);
        self.UploadFileYBtn.hide();

        self.SelectXLbl = QLabel();
        self.SelectXLbl.setText("Select x-data insertion method: ");
        self.Grid.addWidget(self.SelectXLbl, 5, 0);

        self.SelectXBox = QComboBox();
        self.SelectXBox.addItem("Insert data manually");
        self.SelectXBox.addItem("Load data from file");
        self.Grid.addWidget(self.SelectXBox, 5, 1);

        self.OkXBtn = QPushButton("OK");
        self.OkXBtn.clicked.connect(self.plotTypeBtnClicked);
        self.Grid.addWidget(self.OkXBtn, 5, 2);

        self.XDataLine = QLineEdit();
        self.XDataLine.setPlaceholderText("Type array here...");
        self.Grid.addWidget(self.XDataLine, 6, 0, 1, 4);

        self.LoadedXFileLbl = QLabel();
        self.LoadedXFileLbl.setText("No file loaded");
        self.LoadedXFileLbl.setFixedHeight(28);
        self.Grid.addWidget(self.LoadedXFileLbl, 6, 0);
        self.LoadedXFileLbl.hide();

        self.UploadFileXBtn = QPushButton("Upload file");
        self.Grid.addWidget(self.UploadFileXBtn, 6, 1);
        self.UploadFileXBtn.hide();

        self.XBinsLbl = QLabel();
        self.XBinsLbl.setText("No. of bins: ");
        self.XBinsLbl.setAlignment(Qt.AlignRight);
        self.Grid.addWidget(self.XBinsLbl, 6, 0);
        self.XBinsLbl.hide();

        self.XBinsLine = QLineEdit();
        self.XBinsLine.setMaxLength(2);
        self.XBinsLine.setMaximumWidth(20);
        self.Grid.addWidget(self.XBinsLine, 6, 1);
        self.XBinsLine.hide();

        self.PlotBtn = QPushButton("PLOT DATA");
        self.PlotBtn.setFixedHeight(50);
        self.Grid.addWidget(self.PlotBtn, 8, 0, 1, 4);

        self.show();

    # Ensuring correct elements displayed
    def plotTypeBtnClicked(self):
        currPlot: str = self.PlotTypeBox.currentText();
        currXMethod: str = self.SelectXBox.currentText();
        if(((currPlot == "Standard Plot") | (currPlot == "Logarithmic Plot")) & (currXMethod == "Insert data manually")):
            self.XDataLine.show();
            self.XBinsLine.hide();
            self.XBinsLbl.hide();
            self.LoadedXFileLbl.hide();
            self.UploadFileXBtn.hide();
        elif(((currPlot == "Standard Plot") | (currPlot == "Logarithmic Plot")) & (currXMethod == "Load data from file")):
            self.XDataLine.hide();
            self.XBinsLine.hide();
            self.XBinsLbl.hide();
            self.LoadedXFileLbl.show();
            self.UploadFileXBtn.show();
        elif((currPlot == "Histogram") & (currXMethod == "Insert data manually")):
            self.XDataLine.hide();
            self.XBinsLine.show();
            self.XBinsLbl.show();
            self.LoadedXFileLbl.hide();
            self.UploadFileXBtn.hide();
        elif((currPlot == "Histogram") & (currXMethod == "Load data from file")):
            self.XDataLine.hide();
            self.XBinsLine.hide();
            self.XBinsLbl.hide();
            self.LoadedXFileLbl.show();
            self.UploadFileXBtn.show();
    
    def yOkBtnClicked(self):
        currYMethod: str = self.SelectYBox.currentText();
        if(currYMethod == "Insert data manually"):
            self.YDataLine.show();
            self.LoadedYFileLbl.hide();
            self.UploadFileYBtn.hide();
        else:
            self.YDataLine.hide();
            self.LoadedYFileLbl.show();
            self.UploadFileYBtn.show();