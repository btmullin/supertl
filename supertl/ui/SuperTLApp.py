from PySide6 import QtCore, QtWidgets
from supertl.ui import ActivityMapWidget, SuperTLSidebarFrame, ActivityFilterSelectionWidget
from supertl.Data import Activity

class SuperTLApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QtWidgets.QGridLayout(self)

        self.filter = ActivityFilterSelectionWidget.ActivityFilterSelectionWidget()
        self.layout.addWidget(self.filter, 0, 0)

        self.mainview = QtWidgets.QFrame()
        self.mainview_layout = QtWidgets.QGridLayout(self.mainview)

        self.sidebar = SuperTLSidebarFrame.SuperTLSidebarFrame()
        self.mainview_layout.addWidget(self.sidebar,0,0)

        self.selected_file = ""
        self.selected_file_text = QtWidgets.QLabel("No File",
                                     alignment=QtCore.Qt.AlignCenter)
        self.selected_file_text.setStyleSheet("font-size: 20px;")
        self.mainview_layout.addWidget(self.selected_file_text,1,1)

        self.map_view = ActivityMapWidget.ActivityMapWidget()
        # this doesn't work
        # self.map_view.setStyleSheet("margin: 0px 5px 10px 0px;" +
        #                             "border: 10px solid '#FF0000';"+
        #                             "padding: 200px 100px;")
        self.mainview_layout.addWidget(self.map_view, 0,1)

        self.layout.addWidget(self.mainview)

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