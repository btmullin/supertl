from PySide6 import QtCore, QtWidgets
from supertl.ui import SuperTLSidebarFrame, ActivityFilterSelectionWidget, ActivityViewFrame
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

        self.activity_view = ActivityViewFrame.ActivityViewFrame()
        self.mainview_layout.addWidget(self.activity_view, 0,1)

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