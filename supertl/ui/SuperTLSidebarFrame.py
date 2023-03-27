from PySide6 import QtWidgets
from supertl.ui import ActivityButtonsFrame, WorkoutCalendarWidget

class SuperTLSidebarFrame(QtWidgets.QFrame):
    """
    Contains the WorkoutCalendar and ActivityButtons

    Args:
        QFrame (_type_):
    """

    def __init__(self):
        super().__init__()

        self.layout = QtWidgets.QGridLayout(self)

        self.calendar = WorkoutCalendarWidget.WorkoutCalendarWidget()
        self.layout.addWidget(self.calendar, 0, 0)

        self.activity_buttons = ActivityButtonsFrame.ActivityButtonsFrame()
        self.layout.addWidget(self.activity_buttons, 1, 0)

        # benbug - connect buttons to actions