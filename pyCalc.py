# PyCalc : A calculator build using Python and PyQt5
# Importing Libraries
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWidgets import QGridLayout, QLineEdit, QPushButton, QVBoxLayout

__version__ = '0.1'
__author__ = 'Yash Verma'


# Subclass of QMainWindow for calculator GUI, Calculator GUI
class PyCalcUI(QMainWindow):
    def __int__(self):
        # Initialisation
        super().__init__()
        # Setting window properties
        self.setWindowTitle('PyCalc')
        self.setFixedSize(235, 235)
        # Setting central Widget and general layout
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.centralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        # Create display and buttons
        self._createDisplay()
        self._createButtons()

    def _createDisplay(self):
        # Creating display widget
        self.display = QLineEdit()
        # Setting Display Properties
        self.display.setFixedWidth(35)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        # Adding to general layout
        self.generalLayout.addWidget(self.display)

    def _createButtons(self):
        # Creating buttons
        self.buttons = {}
        buttonsLayout = QGridLayout()
        # Button text wrt position on QGridLayout
        buttons = {
            '7': (0,0),
            '8': (0,1),
            '9': (0,2),
            '/': (0,3),
            'C': (0,4),
            '4': (1,0),
            '5': (1,1),
            '6': (1,2),
            '*': (1,3),
            '(': (1,4),
            '1': (2,0),
            '2': (2,1),
            '3': (2,2),
            '-': (2,3),
            ')': (2,4),
            '0': (3,0),
            '00': (3,1),
            '.': (3,2),
            '+': (3,3),
            '=': (3,4),
        }
        # Creating buttons and adding them to GridLayout
        for btnTxt, pos in buttons.items():
            self.buttons[btnTxt] = QPushButton(btnTxt)
            self.buttons[btnTxt].setFixedSize(40,40)
            buttonsLayout.addWidget(self.buttons[btnTxt], pos[0], pos[1])
            # Add buttons to general layout
            self.generalLayout.addLayout(buttonsLayout)

    def setDisplayText(self,text):
        # Set display's text
        self.display.setText(text)
        self.display.setFocus()

    def displayText(self):
        # Get display's text
        return self.display.text()

    def clearDisplay(self):
        # Clear display
        self.setDisplayText('')

# Main Function
def main():
    # Creating instance of QApplication
    pycalc = QApplication(sys.argv)
    # Show calculator GUI
    view = PyCalcUI()
    view.show()
    # Execute calculator main loop
    sys.exit(pycalc.exec())


if __name__ == '__main__':
    main()
