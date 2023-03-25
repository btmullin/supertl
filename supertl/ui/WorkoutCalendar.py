from PySide6 import QtCore, QtWidgets, QtGui

class WorkoutCalendar(QtWidgets.QCalendarWidget):
    def __init__(self):
        super().__init__()
        self.selectionMode = QtWidgets.QCalendarWidget.SelectionMode.SingleSelection

    def paintCell(self, painter: QtGui.QPainter, rect: QtCore.QRect, date: QtCore.QDate) -> None:
        super().paintCell(painter, rect, date)
        
        # benbug - do special stuff here when we figure out the architecture to have workouts selected
        # highlight that date
        #if date.day() == 5:
        #    painter.save()
        #    painter.drawEllipse(rect)
        #    painter.restore()
