import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/MainWin.ui', self)


def except_hook(a, b, c):
    sys.__excepthook__(a, b, c)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
