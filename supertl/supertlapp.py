import sys
from PySide6 import QtCore, QtWidgets
from PySide6.QtWebEngineWidgets import QWebEngineView
from supertl.ui import WorkoutCalendar

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.select_activity_button = QtWidgets.QPushButton("Select activity file")

        self.layout = QtWidgets.QGridLayout(self)
        self.layout.addWidget(self.select_activity_button,1,0)

        self.workout_calendar = WorkoutCalendar.WorkoutCalendar()
        self.layout.addWidget(self.workout_calendar,0,0)

        self.selected_file = ""
        self.selected_file_text = QtWidgets.QLabel("No File",
                                     alignment=QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.selected_file_text,1,1)

        self.webEngineView = QWebEngineView()
        f = open('c:/git/supertl/devplayground/map.html','r')
        self.webEngineView.setHtml(f.read())
        self.layout.addWidget(self.webEngineView,0,1)

        # place to render the map
        # place to render a graph
        # place to display the workout summary

        self.select_activity_button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        # benbug - open file dialog
        filechooser = QtWidgets.QFileDialog(self, caption="Select Activity File", filter="Activity Files (*.fit)")
        filechooser.setFileMode(QtWidgets.QFileDialog.FileMode.ExistingFile)
        if (filechooser.exec()):
            self.selected_file = filechooser.selectedFiles()[0]
        self.selected_file_text.setText(self.selected_file)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())