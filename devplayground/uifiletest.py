import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtCore import QFile
from supertl.ui.supertlui import Ui_supertl_ui

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_supertl_ui()
        self.ui_widget = QWidget()
        self.setCentralWidget(self.ui_widget)
        self.ui.setupUi(self.ui_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())