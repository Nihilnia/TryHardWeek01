from PyQt5.QtWidgets import QApplication, QVBoxLayout, QPushButton, QTextEdit, QWidget
import sys


class Window(QWidget):

    def __init__(self):

        super().__init__()
        self.userInterface()

    def userInterface(self):

        self.textEdit01 = QTextEdit()
        self.buttonClear = QPushButton("Clear")

        vBox = QVBoxLayout()
        vBox.addWidget(self.textEdit01)
        vBox.addWidget(self.buttonClear)

        self.setWindowTitle("Day One, exercise 3!")
        self.setLayout(vBox)

        self.buttonClear.clicked.connect(self.whenClicked)

        self.show()

    def whenClicked(self):
        self.textEdit01.clear()

myApp = QApplication(sys.argv)

createIt = Window()

sys.exit(myApp.exec_())