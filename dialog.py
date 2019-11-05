# Dialog-Style Application
# Importing libraries
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QDialogButtonBox
from PyQt5.QtWidgets import QLineEdit

# Dialog Class
class Dialog(QDialog):
    # Initialize 
    def __init__(self,parent = None):
        super().__init__(parent)
        self.setWindowTitle("QDialog")
        dlgLayout = QVBoxLayout()
        formLayout = QFormLayout()
        formLayout.addRow('Name: ',QLineEdit())
        formLayout.addRow('Age: ',QLineEdit())
        formLayout.addRow('Hobbies: ',QLineEdit())
        dlgLayout.addLayout(formLayout)
        btns = QDialogButtonBox()
        btns.setStandardButtons(
                QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        dlgLayout.addWidget(btns)
        self.setLayout(dlgLayout)

if __name__ == '__main__':
    app = QApplication([])
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())
