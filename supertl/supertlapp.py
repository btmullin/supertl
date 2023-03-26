import sys
from PySide6 import QtWidgets
from supertl.ui import SuperTLApp

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    with open('supertl/ui/supertl.qss', encoding='utf-8') as style_file:
        style = style_file.read()
    app.setStyleSheet(style)

    screen_rect = app.primaryScreen().geometry()
    inset = 30

    gui = SuperTLApp.SuperTLApp()
    gui.setWindowTitle("Super Training Log")
    gui.resize(screen_rect.width()-inset*2, screen_rect.height()-inset*2-80)
    gui.move(screen_rect.top()+inset, screen_rect.left()+inset)
    gui.show()

    sys.exit(app.exec())
