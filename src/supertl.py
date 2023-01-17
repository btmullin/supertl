import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from WorkoutCalendar import WorkoutCalendar

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World",
                                     alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QGridLayout(self)
        self.layout.addWidget(self.text,0,1)
        self.layout.addWidget(self.button,0,2)

        self.cal = QtWidgets.QCalendarWidget()
        self.cal.setGridVisible(False)

        self.layout.addWidget(self.cal,0,0)

        self.wc = WorkoutCalendar()
        self.layout.addWidget(self.wc,0,4)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())