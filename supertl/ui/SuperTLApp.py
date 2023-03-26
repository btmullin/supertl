from PySide6 import QtCore, QtWidgets
from supertl.ui import WorkoutCalendar, ActivityMapWidget, ActivityButtons
from supertl.Data import Activity

class SuperTLApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QtWidgets.QGridLayout(self)

        self.workout_calendar = WorkoutCalendar.WorkoutCalendar()
        self.layout.addWidget(self.workout_calendar,0,0)

        self.activity_buttons = ActivityButtons.ActivityButtons()
        self.layout.addWidget(self.activity_buttons,1,0)

        self.selected_file = ""
        self.selected_file_text = QtWidgets.QLabel("No File",
                                     alignment=QtCore.Qt.AlignCenter)
        self.selected_file_text.setStyleSheet("font-size: 20px;")
        self.layout.addWidget(self.selected_file_text,1,1)

        self.map_view = ActivityMapWidget.ActivityMapWidget()
        # this doesn't work
        # self.map_view.setStyleSheet("margin: 0px 5px 10px 0px;" +
        #                             "border: 10px solid '#FF0000';"+
        #                             "padding: 200px 100px;")
        self.layout.addWidget(self.map_view, 0,1)

        # place to render a graph
        # place to display the workout summary


    @QtCore.Slot()
    def magic(self):
        filechooser = QtWidgets.QFileDialog(self,
                                            caption="Select Activity File",
                                            filter="Activity Files (*.fit)")
        filechooser.setFileMode(QtWidgets.QFileDialog.FileMode.ExistingFile)
        if filechooser.exec():
            self.selected_file = filechooser.selectedFiles()[0]
            activity = Activity.Activity(self.selected_file)
            self.map_view.set_activity(activity)
        self.selected_file_text.setText(self.selected_file)