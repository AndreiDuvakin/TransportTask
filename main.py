import sys

from PyQt5.QtWidgets import QApplication

from MainWindow import MainWin


def except_hook(a, b, c):
    sys.__excepthook__(a, b, c)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
