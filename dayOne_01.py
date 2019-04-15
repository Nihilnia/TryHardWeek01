from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QCheckBox, QApplication, QVBoxLayout
from sys import argv, exit

class Window(QWidget):

    def __init__(self):

        super().__init__()
        self.userInterface()

    def userInterface(self):

        self.checkBox01 = QCheckBox("Are you ready?")
        self.checkBox02 = QCheckBox("TRYHARD?")
        self.label01 = QLabel()
        self.button01 = QPushButton("Click!")

        vBox = QVBoxLayout()
        vBox.addWidget(self.checkBox01)
        vBox.addWidget(self.checkBox02)
        vBox.addWidget(self.label01)
        vBox.addWidget(self.button01)

        self.setWindowTitle("Day One")
        self.setLayout(vBox)

        self.button01.clicked.connect(lambda : self.whenClicked(self.checkBox01.isChecked(), self.checkBox02.isChecked()))

        self.show()
    
    def whenClicked(self, checkBox01, checkBox02):
        if checkBox01 and checkBox02:
            self.label01.setText("FIREEEEEEEEEEEEEE!")
        elif checkBox01:
            self.label01.setText("Ofc you're ready!")
        elif checkBox02:
            self.label01.setText("HELL YEAH!")
        else:
            self.label01.setText("There is no option like that!")

    


myApp = QApplication(argv)

createIt = Window()

exit(myApp.exec_())