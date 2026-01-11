
import sys
from PyQt5.QtWidgets import QApplication, QWidget,QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout,QHBoxLayout,QPushButton


class Counter(QWidget):

    def __init__(self):
        super().__init__()
        self.expression = ""
        self.setGeometry(750,300,500,500)
        self.label=QLabel(self) #remember that the label is the main number we are displaying basically... and the label always displays as strings
        self.b1=QPushButton("1", self)
        self.b2=QPushButton("2", self)
        self.b3=QPushButton("3", self)
        self.b4=QPushButton("4", self)
        self.b5=QPushButton("5", self)
        self.b6=QPushButton("6", self)
        self.b7=QPushButton("7", self)
        self.b8=QPushButton("8", self)
        self.b9=QPushButton("9", self)
        self.b0=QPushButton("0", self)
        self.bp=QPushButton("+", self)
        self.bm=QPushButton("-", self)
        self.bx=QPushButton("*", self)
        self.bd=QPushButton("/", self)
        self.bf=QPushButton(".", self)
        self.be=QPushButton("=", self)
        self.initUI()

    def initUI(self):

        self.setWindowTitle("CALCULATOR")

        self.setFocus()

        #label designing
        self.label.setText("")
        self.label.setStyleSheet("font-size: 150px")
        self.label.setAlignment(Qt.AlignCenter)

        #button designing
        self.b1.setStyleSheet("font-size: 30px")
        self.b2.setStyleSheet("font-size: 30px")
        self.b3.setStyleSheet("font-size: 30px")
        self.b4.setStyleSheet("font-size: 30px")
        self.b5.setStyleSheet("font-size: 30px")
        self.b6.setStyleSheet("font-size: 30px")
        self.b7.setStyleSheet("font-size: 30px")
        self.b8.setStyleSheet("font-size: 30px")
        self.b9.setStyleSheet("font-size: 30px")
        self.b0.setStyleSheet("font-size: 30px")
        self.bp.setStyleSheet("font-size: 30px")
        self.bm.setStyleSheet("font-size: 30px")
        self.bx.setStyleSheet("font-size: 30px")
        self.bd.setStyleSheet("font-size: 30px")
        self.bf.setStyleSheet("font-size: 30px")
        self.be.setStyleSheet("font-size: 30px")

        #layout for buttons horizontally
        hbox1=QHBoxLayout()
        hbox1.addWidget(self.b1)
        hbox1.addWidget(self.b2)
        hbox1.addWidget(self.b3)
        hbox1.addWidget(self.bp)

        hbox2=QHBoxLayout()
        hbox2.addWidget(self.b4)
        hbox2.addWidget(self.b5)
        hbox2.addWidget(self.b6)
        hbox2.addWidget(self.bm)

        hbox3=QHBoxLayout()
        hbox3.addWidget(self.b7)
        hbox3.addWidget(self.b8)
        hbox3.addWidget(self.b9)
        hbox3.addWidget(self.bx)

        hbox4=QHBoxLayout()
        hbox4.addWidget(self.bf)
        hbox4.addWidget(self.b0)
        hbox4.addWidget(self.bd)
        hbox4.addWidget(self.be)

        #layout for buttons and label vertically
        vbox=QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addLayout(hbox1) #hbox is a layout so using addwidget wont work
        vbox.addLayout(hbox2) #hbox is a layout so using addwidget wont work
        vbox.addLayout(hbox3) #hbox is a layout so using addwidget wont work
        vbox.addLayout(hbox4) #hbox is a layout so using addwidget wont work
        self.setLayout(vbox)
        
        #functionality connections
        self.b1.clicked.connect(self.add_to_expression)
        self.b2.clicked.connect(self.add_to_expression)
        self.b3.clicked.connect(self.add_to_expression)
        self.b4.clicked.connect(self.add_to_expression)
        self.b5.clicked.connect(self.add_to_expression)
        self.b6.clicked.connect(self.add_to_expression)
        self.b7.clicked.connect(self.add_to_expression)
        self.b8.clicked.connect(self.add_to_expression)
        self.b9.clicked.connect(self.add_to_expression)
        self.b0.clicked.connect(self.add_to_expression)
        self.bp.clicked.connect(self.add_to_expression)
        self.bm.clicked.connect(self.add_to_expression)
        self.bx.clicked.connect(self.add_to_expression)
        self.bd.clicked.connect(self.add_to_expression)
        self.bf.clicked.connect(self.add_to_expression)
        self.be.clicked.connect(self.calculate)

    def add_to_expression(self):
        button = self.sender()           # which button was clicked
        self.expression += button.text() # append its text
        self.label.setText(self.expression)

    def calculate(self):
        try:
            result = str(eval(self.expression))
            self.label.setText(result)
            self.expression = result   # allows chaining (e.g. 5 + 2 + 3)
        except:
            self.label.setText("Error")
            self.expression = ""

def main():
    app=QApplication(sys.argv)
    counter=Counter()
    counter.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()
