from PySide6 import QtCore, QtWidgets, QtGui

class WorkoutCalendar(QtWidgets.QCalendarWidget):
    def __init__(self):
        super().__init__()

    def paintCell(self, painter: QtGui.QPainter, rect: QtCore.QRect, date: QtCore.QDate) -> None:
        if date.day() == 5:
            painter.save()
            painter.drawEllipse(rect)
            painter.restore()
        else:
            super().paintCell(painter, rect, date)