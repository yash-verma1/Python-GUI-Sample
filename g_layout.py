# PyQt5 Grid Layout Example
# Importing Libraries
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget

app = QApplication([]) # Passing empty arguments

window = QWidget()
window.setWindowTitle("GridLayout")
layout = QGridLayout()
layout.addWidget(QPushButton('0,0'),0,0)    # 2nd and 3rd argument specify position of the widget
layout.addWidget(QPushButton('0,1'),0,1)
layout.addWidget(QPushButton('0,2'),0,2)
layout.addWidget(QPushButton('1,0'),1,0)
layout.addWidget(QPushButton('1,1'),1,1)
layout.addWidget(QPushButton('1,2'),1,2)
layout.addWidget(QPushButton('2,0'),2,0)
layout.addWidget(QPushButton('2,1 + 2 column Span'),2,1,1,2) # 4th and 5th argument specify row span and column span 
window.setLayout(layout)
window.show()

sys.exit(app.exec_())
