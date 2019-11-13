# A simple calculator built using Python and PyQt5

# Importing required libraries
import sys
from functools import partial
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWidgets import QGridLayout, QLineEdit, QPushButton, QVBoxLayout

__version__ = '0.1'
__author__ = 'Yash Verma'

# Global Variables
ERROR_MSG = 'ERROR'

# Calculator UI Class
class PyCalcUI(QMainWindow):
    # View Initializer
    def __init__(self):
        super().__init__()
        # Setting window properties
        self.setWindowTitle('PyCalc')
        self.setFixedSize(235,235)
        # Setting central widget and general layout
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        # Creating the display and the buttons
        self._createDisplay()
        self._createButtons()
    
    # Creates the display
    def _createDisplay(self):
        # Creating the display widget
        self.display = QLineEdit()
        # Setting display properties
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        # Adding display to general layout
        self.generalLayout.addWidget(self.display)

    # Creates the buttons
    def _createButtons(self):
        self.buttons = {}
        buttonsLayout = QGridLayout()
        # setting up a dictionary with button text and grid layout position
        buttons = {
                '7':(0,0),
                '8':(0,1),
                '9':(0,2),
                '/':(0,3),
                'C':(0,4),
                '4':(1,0),
                '5':(1,1),
                '6':(1,2),
                '*':(1,3),
                '(':(1,4),
                '1':(2,0),
                '2':(2,1),
                '3':(2,2),
                '-':(2,3),
                ')':(2,4),
                '0':(3,0),
                '00':(3,1),
                '.':(3,2),
                '+':(3,3),
                '=':(3,4),
                }
        # Creating buttons and adding them to grid layout
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(40,40)
            buttonsLayout.addWidget(self.buttons[btnText], pos[0] , pos[1])
        
        # Adding buttons to general layout
        self.generalLayout.addLayout(buttonsLayout)

    # Set display's text
    def setDisplayText(self, text):
        self.display.setText(text)
        self.display.setFocus()

    # Get display's text
    def displayText(self):
        return self.display.text()

    # Clear display's text
    def clearDisplay(self):
        self.setDisplayText('')


# PyCalc Controller Class
class PyCalcCtrl:
    # Initialising
    def __init__(self,model,view):
        self._evaluate = model
        self._view = view
        # Connecting signals and slots
        self._connectSignals()

    # Evaluate expressions
    def _calculateResult(self):
        result = self._evaluate(expression=self._view.displayText())
        self._view.setDisplayText(result)

    # Function for building expressions
    def _buildExpression(self, sub_exp):
        if self._view.displayText() == ERROR_MSG:
            self._view.clearDisplay()

        expression = self._view.displayText() + sub_exp
        self._view.setDisplayText(expression)

    # Function to connect signals and slots
    def _connectSignals(self):
        for btnText, btn in self._view.buttons.items():
            if btnText not in {'=','C'}:
                btn.clicked.connect(partial(self._buildExpression,btnText))

        self._view.buttons['='].clicked.connect(self._calculateResult)
        self._view.display.returnPressed.connect(self._calculateResult)
        self._view.buttons['C'].clicked.connect(self._view.clearDisplay)


# Model to evaluate calculator expressions
def evaluateExpression(expression):
    try:
        result = str(eval(expression, {}, {}))
    except Exception:
        result = ERROR_MSG

    return result



# Main Function
def main():
    # Creating instatnce of QApplication
    pycalc = QApplication(sys.argv)
    # Show calculator UI
    view = PyCalcUI()
    view.show()
    # Creating instance of model and controller
    model = evaluateExpression
    PyCalcCtrl(model=model, view=view)
    # Execute application's main loop
    sys.exit(pycalc.exec())

if __name__ == '__main__':
    main()
