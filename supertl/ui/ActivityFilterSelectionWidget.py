from PySide6 import QtWidgets

class ActivityFilterSelectionWidget(QtWidgets.QFrame):
    """
    Filter Selection

    Args:
        QFrame (_type_):
    """

    def __init__(self):
        super().__init__()

        self.layout = QtWidgets.QGridLayout(self)

        self.place_holder = QtWidgets.QPushButton("Activity Filter Selection Placeholder")
        self.layout.addWidget(self.place_holder)

        # benbug - Implement a filter selection