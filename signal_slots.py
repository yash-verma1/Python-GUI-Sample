# Signals and slots example
# Importing Libraries
import sys

from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget
import functools

# No arguments passed
def greeting():
    # Slot function
    if msg.text():
        msg.setText('')
    else:
        # Simple Pre-defined Text
        msg.setText("Hello World!")

# Passing argument for name
def greeting(who):
    # Slot function with arguments
    if msg.text():
        msg.setText('')
    else:
        # Pass argument to greeting text
        msg.setText(f"Hello {who}")

app = QApplication([])
window = QWidget()
window.setWindowTitle('Signals and Slots')
layout = QVBoxLayout()

btn = QPushButton('Greet')
# Connect clicked event to greeting()

# Simple connect
#btn.clicked.connect(greeting)
btn.clicked.connect(functools.partial(greeting,'Yash!'))

layout.addWidget(btn)
msg = QLabel('')
layout.addWidget(msg)
window.setLayout(layout)
window.show()
sys.exit(app.exec())
