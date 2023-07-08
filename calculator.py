import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6 import QtCore
from UI.calculator_ui import Ui_Calculator

class Calculator(QWidget, Ui_Calculator):

    def __init__(self):
        super().__init__()
        # sets up the UI
        self.setupUi(self)

        # connects the pushbutton signals to the slots
        # this checks if the numbers or decimal have been clicked
        self.pb_0.clicked.connect(self.number_clicked)
        self.pb_1.clicked.connect(self.number_clicked)
        self.pb_2.clicked.connect(self.number_clicked)
        self.pb_3.clicked.connect(self.number_clicked)
        self.pb_4.clicked.connect(self.number_clicked)
        self.pb_5.clicked.connect(self.number_clicked)
        self.pb_6.clicked.connect(self.number_clicked)
        self.pb_7.clicked.connect(self.number_clicked)
        self.pb_8.clicked.connect(self.number_clicked)
        self.pb_9.clicked.connect(self.number_clicked)
        self.pb_decimal.clicked.connect(self.number_clicked)

        # this checks if the operators or clear buttons have been clicked
        self.pb_multiply.clicked.connect(self.multiply_clicked)
        self.pb_divide.clicked.connect(self.divide_clicked)
        self.pb_subtract.clicked.connect(self.subtract_clicked)
        self.pb_add.clicked.connect(self.add_clicked)
        self.pb_equals.clicked.connect(self.equals_clicked)
        self.pb_clearAll.clicked.connect(self.clear_all_clicked)
        self.pb_clearCurrent.clicked.connect(self.clear_current_clicked)

        # variables to be used to store the numbers and operator used by the calculator
        self.active_num = ''
        self.first_num = ''
        self.operator = ''


    # defines a Qt slot decorator 
    @QtCore.Slot()
    def number_clicked(self):
        # the .sender() connects to the number_clicked signal
        button_value = self.sender()
        
        # makes it so that the user can only add one decimal point
        # checks to see if a decimal point is present and if it isn't it adds one
        # if it is present it continues to the else
        if button_value.text() == '.':
            if '.' not in self.active_num:
                self.active_num += button_value.text()
                self.calc_num.setText(self.active_num)
        else:
            # won't allow the active num to be higher than 9 digits
            # returns the active num if it is higher than 9 digits
            if len(self.active_num) > 8:
                return self.active_num

            # adds the button_value to the active_num string
            self.active_num += button_value.text()
            # updates the calc_num viewer to show the active num string
            self.calc_num.setText(self.active_num)


    # when X is clicked the current first_num variable is set to the value of active_num variable
    # the active_num variable is reset and operator is set to the operator
    @QtCore.Slot()
    def multiply_clicked(self):
        self.first_num = self.active_num
        self.active_num = ''
        self.operator = self.sender()
        return self.operator.text()


    # when / is clicked the current first_num variable is set to the value of active_num variable
    # the active_num variable is reset and operator is set to the operator
    @QtCore.Slot()
    def divide_clicked(self):
        self.first_num = self.active_num
        self.active_num = ''
        self.operator = self.sender()
        return self.operator.text()


    # when - is clicked the current first_num variable is set to the value of active_num variable
    # the active_num variable is reset and operator is set to the operator
    @QtCore.Slot()
    def subtract_clicked(self):
        # logic for negative numbers
        # if active_num hasn't been set yet and minus is clicked the number will be negative
        if self.active_num == '':
            self.active_num += '-'
            return self.active_num
        
        # if first_num has been set and minus is clicked the new active num will be negative
        if self.first_num != '':
            self.active_num += '-'
            return self.active_num
        
        self.first_num = self.active_num
        self.active_num = ''
        self.operator = self.sender()
        return self.operator.text()


    # when X is clicked the current first_num variable is set to the value of active_num variable
    # the active_num variable is reset and operator is set to the operator
    @QtCore.Slot()
    def add_clicked(self):
        self.first_num = self.active_num
        self.active_num = ''
        self.operator = self.sender()
        return self.operator.text()


    @QtCore.Slot()
    def equals_clicked(self):

        # logic for multiplication
        # the first_num and active_num variables are first converted to floats    
        if self.operator.text() == 'X':
            equals_num = float(self.first_num) * float(self.active_num)

        # logic for division 
        elif self.operator.text() == '/':
            # if you try to divide by 0 you receive an error
            if self.active_num == '0':
                self.calc_num.setText('Error / 0')
                self.active_num = ''
                self.first_num = ''
                self.operator = ''
                return self.active_num
            else:
                equals_num = float(self.first_num) / float(self.active_num)

        # logic for subtraction
        elif self.operator.text() == '-':
            equals_num = float(self.first_num) - float(self.active_num)

        # logic for addition 
        elif self.operator.text() == '+':
            equals_num = float(self.first_num) + float(self.active_num)

        # rounds equals_num to 2 decimal places
        equals_num = round(equals_num, 2)

        # if the value of this is greater than 9 digits an out of range message is shown
        # the values of active_num, first_num, and operator are reset
        if equals_num > 999999999 or equals_num < -999999999:
            self.calc_num.setText('Out Of Range')
            self.active_num = ''
            self.first_num = ''
            self.operator = ''
            return self.active_num, self.first_num, self.operator

        # if the value is less than 9 digits the equals_num value is converted to a string
        # the equals_num is displayed on the calc_num screen
        # active_num is set to the value of str(equals_num)
        # first_num and operator are reset
        else:
            self.calc_num.setText(str(equals_num))
            self.active_num = str(equals_num)
            self.first_num = ''
            self.operator = ''
            return self.active_num, self.first_num, self.operator


    # when CE is clicked active_num, first_num and operator are reset
    # the calc_num screen is set to show 0
    @QtCore.Slot()
    def clear_all_clicked(self):
        self.active_num = ''
        self.first_num = ''
        self.operator = ''
        self.calc_num.setText('0')
        return self.active_num, self.first_num, self.operator

    # when C is clicked the current active_num is reset
    # the calc_num screen is set to show 0
    @QtCore.Slot()
    def clear_current_clicked(self):
        self.active_num = ''
        self.calc_num.setText('0')
        return self.active_num


#creates an instance of QApplication and executes the program
if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Calculator()
    window.show()

    # terminates the program if it is exited
    sys.exit(app.exec())