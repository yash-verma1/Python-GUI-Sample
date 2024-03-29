# Main-Window Style Application
# Importing Libraries
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtWidgets import QToolBar

# Class for Main Window
class Window(QMainWindow):
    def __init__(self,parent=None):
        # Initializer
        super().__init__(parent)
        self.setWindowTitle('QMainWindow')
        self.setCentralWidget(QLabel('Central Widget'))
        self._createMenu()
        self._createToolBar()
        self._createStatusBar()

    def _createMenu(self):
        # added space for Mac OS, no space required for Windows/Linux
        self.menu = self.menuBar().addMenu(" &Menu")
        self.menu.addAction(" &Exit",self.close)

    def _createToolBar(self):
        tools = QToolBar()
        self.addToolBar(tools)
        tools.addAction('Exit',self.close)

    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage("Status Bar")
        self.setStatusBar(status)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
