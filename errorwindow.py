from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton;
from PyQt5.QtGui import QFont;
from PyQt5.QtCore import Qt;


class ErrorWindow(QWidget):
    # Properties
    ErrorMsg: str;

    # Size properties
    XSize: int;
    YSize: int;

    # Layout
    Grid: QGridLayout;

    # Elements
    ErrorLbl: QLabel;
    OkBtn: QPushButton;

    # Initialization
    def __init__(self, errorCause: str):
        super().__init__();
        self.XSize = 250;
        self.YSize = 100;
        self.setWindowModality(Qt.ApplicationModal);
        self.setFixedSize(self.XSize, self.YSize);
        self.setFont(QFont("Arial", 10));
        self.setWindowTitle("ERROR");

        self.Grid = QGridLayout(self);

        self.ErrorLbl = QLabel();
        self.ErrorLbl.setAlignment(Qt.AlignCenter);
        self.Grid.addWidget(self.ErrorLbl);

        self.OkBtn = QPushButton("OKAY");
        self.OkBtn.clicked.connect(self.okBtnClicked);
        self.Grid.addWidget(self.OkBtn, 1, 0, alignment=Qt.AlignCenter);

        if(errorCause == "Unknown File"):
            self.ErrorMsg = "Unknown file was selected";
            self.ErrorLbl.setText(self.ErrorMsg);
        elif(errorCause == "No Path"):
            self.ErrorMsg = "No path was selected";
            self.ErrorLbl.setText(self.ErrorMsg);
        elif(errorCause == "Y Value Error"):
            self.ErrorMsg = "Invalid Y values";
            self.ErrorLbl.setText(self.ErrorMsg);
        elif(errorCause == "X Value Error"):
            self.ErrorMsg = "Invalid X values";
            self.ErrorLbl.setText(self.ErrorMsg);
        
        self.show();
    
    # Leave Error Window
    def okBtnClicked(self):
        self.close();