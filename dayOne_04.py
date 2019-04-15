from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit
import sys, random


class NotePad(QWidget):

    def __init__(self):

        super().__init__()
        self.userInterface()

    def userInterface(self):

        self.textArea = QTextEdit()
        self.buttonClear = QPushButton("Clear")
        self.buttonSave = QPushButton("Save")

        vBox = QVBoxLayout()
        vBox.addWidget(self.textArea)
        vBox.addWidget(self.buttonClear)
        vBox.addWidget(self.buttonSave)

        self.setWindowTitle("Day One Let's gooo!")
        self.setLayout(vBox)

        self.buttonClear.clicked.connect(self.whenClicked)
        self.buttonSave.clicked.connect(self.whenClicked)

        self.show()

    def whenClicked(self):

        sender = self.sender()

        if sender.text() == "Clear":
            self.textArea.clear()
        elif sender.text() == "Save":
            fileName = str(random.randint(1, 100)) + ".txt"
            newFile = open(fileName, "a", encoding = "utf-8")
            newFile.write(self.textArea.toPlainText())
            sys.exit()
            
myApp = QApplication(sys.argv)

createIt = NotePad()

sys.exit(myApp.exec_())