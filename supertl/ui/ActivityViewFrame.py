from PySide6 import QtWidgets, QtCore
from supertl.ui import ActivityMapWidget

class ActivityViewFrame(QtWidgets.QFrame):
    """
    Contains the AcitivtySummaryFrame and ActivityMapWidget

    Args:
        QFrame (_type_):
    """

    def __init__(self):
        super().__init__()

        self.layout = QtWidgets.QSplitter(self, QtCore.Qt.Orientation.Horizontal)
        self.layout.setHandleWidth(5)

        self.summary_frame = QtWidgets.QLabel("SUMMARY FRAME PLACEHOLDER")
        self.layout.addWidget(self.summary_frame)

        self.activity_map = ActivityMapWidget.ActivityMapWidget()
        self.layout.addWidget(self.activity_map)

        # benbug - connect buttons to actions