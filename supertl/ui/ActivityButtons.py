from PySide6 import QtWidgets

class ActivityButtons(QtWidgets.QFrame):
    """
    WorkoutButtons displays a set of buttons that enable the addition/import/export/delete/etc
    of individual activites.

    Args:
        QFrame (_type_):
    """

    def __init__(self):
        super().__init__()

        self.layout = QtWidgets.QGridLayout(self)

        self.add_button = QtWidgets.QPushButton("Add")
        self.layout.addWidget(self.add_button,0,0)
        self.import_button = QtWidgets.QPushButton("Import")
        self.layout.addWidget(self.import_button,1,0)
        self.delete_button = QtWidgets.QPushButton("Delete")
        self.layout.addWidget(self.delete_button,2,0)
        self.export_button = QtWidgets.QPushButton("Export")
        self.layout.addWidget(self.export_button,3,0)

        # benbug - connect buttons to actions