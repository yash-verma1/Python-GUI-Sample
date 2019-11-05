# Hello World PyQt5
# import sys to handle exit status for the Qt window
import sys

# Required Qt widgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

# Create instance of QApplication
app = QApplication(sys.argv)

# Create instance of application GUI
window = QWidget()
window.setWindowTitle('PyQt5 App')
window.setGeometry(100,100,280,80)
window.move(60,15)
helloMsg = QLabel('<h1>Hello World!</h1>',parent=window)
helloMsg.move(60,15)

# Show app
window.show()

# Run application's event loop (main loop)
sys.exit(app.exec_())
