from PySide6 import QtWidgets

class WorkoutCalendarWidget(QtWidgets.QFrame):
    """
    WorkoutCalendar displays a calendar view associated with a log book and
    will indicate what days have activities associated with them and will allow
    selection that will modify the selected week/activity

    Args:
        QFrame (_type_):
    """
    num_cals = 2

    def __init__(self):
        super().__init__()

        self.layout = QtWidgets.QGridLayout(self)

        self.cal = []
        for i in range(self.num_cals):
            self.cal.append(QtWidgets.QCalendarWidget())
            self.cal[i].selectionMode = QtWidgets.QCalendarWidget.SelectionMode.SingleSelection
            self.cal[i].setGridVisible(True)
            if i > 0:
                for _ in range(i):
                    self.cal[i].showNextMonth()
            # benbug - would like to disable the navigation buttons only, not the month name display
            # if i > 0:
            #     self.cal[i].setNavigationBarVisible(False)
            self.layout.addWidget(self.cal[i],i,0)
        #self.setMaximumWidth(400)

    # benbug - do special stuff here when we figure out the architecture to have workouts selected
    # def paintCell(self, painter: QtGui.QPainter, rect: QtCore.QRect, date: QtCore.QDate) -> None:
    #     super().paintCell(painter, rect, date)

        # highlight that date
        #if date.day() == 5:
        #    painter.save()
        #    painter.drawEllipse(rect)
        #    painter.restore()
