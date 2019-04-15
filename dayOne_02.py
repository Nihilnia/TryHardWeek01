from PyQt5.QtWidgets import QApplication, QPushButton, QRadioButton, QLabel, QWidget, QVBoxLayout
import sys


class Window(QWidget):

    def __init__(self):

        super().__init__()
        self.userInterface()


    def userInterface(self):

        self.headLine = QLabel("What's your fav color?")
        self.result = QLabel("")
        self.red = QRadioButton("Red")
        self.yellow = QRadioButton("Yellow")
        self.blue = QRadioButton("Blue")
        self.button01 = QPushButton("Check..")

        vBox = QVBoxLayout()
        vBox.addWidget(self.headLine)
        vBox.addWidget(self.red)
        vBox.addWidget(self.yellow)
        vBox.addWidget(self.blue)
        vBox.addStretch()
        vBox.addWidget(self.result)
        vBox.addWidget(self.button01)


        self.setWindowTitle("Day One!")
        self.setLayout(vBox)

        self.button01.clicked.connect(lambda : self.whenClicked(self.red.isChecked(), self.yellow.isChecked(), self.blue.isChecked()))

        self.show()

    def whenClicked(self, color1, color2, color3):

        if color1:
            self.result.setText("Red wine!")
        elif color2:
            self.result.setText("Yellow shit!")
        elif color3:
            self.result.setText("Blue blood!")
        else:
            self.result.setText("Select once!")





myApp = QApplication(sys.argv)

createIt = Window()

sys.exit(myApp.exec_())