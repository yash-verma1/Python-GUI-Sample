# PyQt Vertical Layout Example
# Importing libraries
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("VBox Layout Example")
layout = QVBoxLayout()
layout.addWidget(QPushButton("Top"))
layout.addWidget(QPushButton("Middle"))
layout.addWidget(QPushButton("Bot"))
window.setLayout(layout)
window.show()

sys.exit(app.exec_())
