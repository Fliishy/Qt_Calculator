import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6 import QtCore
from UI.calculator_ui import Ui_Calculator

class Calculator(QWidget, Ui_Calculator):

    def __init__(self):
        super().__init__()
        # sets up the UI
        self.setupUi(self)

        # connects the pushbutton signals to the slot button_clicked
        # this checks if the buttons have been clicked
        self.pb_0.clicked.connect(self.button_clicked)
        self.pb_1.clicked.connect(self.button_clicked)
        self.pb_2.clicked.connect(self.button_clicked)
        self.pb_3.clicked.connect(self.button_clicked)
        self.pb_4.clicked.connect(self.button_clicked)
        self.pb_5.clicked.connect(self.button_clicked)
        self.pb_6.clicked.connect(self.button_clicked)
        self.pb_7.clicked.connect(self.button_clicked)
        self.pb_8.clicked.connect(self.button_clicked)
        self.pb_9.clicked.connect(self.button_clicked)
        self.pb_multiply.clicked.connect(self.button_clicked)
        self.pb_divide.clicked.connect(self.button_clicked)
        self.pb_subtract.clicked.connect(self.button_clicked)
        self.pb_add.clicked.connect(self.button_clicked)
        self.pb_equals.clicked.connect(self.button_clicked)
        self.pb_decimal.clicked.connect(self.button_clicked)
        self.pb_clearAll.clicked.connect(self.button_clicked)
        self.pb_clearCurrent.clicked.connect(self.button_clicked)

    # defines a Qt slot decorator 
    @QtCore.Slot()
    def button_clicked(self):
        # the .sender() connects to the button_clicked signal
        self.button_value = self.sender()
        # updates the calc_num viewer to show what button was last pressed
        self.calc_num.setText(self.button_value.text())
        # returns the buttons text value when the button clicked signal is received
        return self.button_value.text()


#creates an instance of QApplication and executes the program
if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Calculator()
    window.show()

    # terminates the program if it is exited
    sys.exit(app.exec())