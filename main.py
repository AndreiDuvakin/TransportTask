import sys

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication

from main_window import MainWin
from splash_screen import SplashScreen


def except_hook(a, b, c):
    sys.__excepthook__(a, b, c)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    splash = SplashScreen()
    splash.show()

    win = MainWin()

    QTimer.singleShot(3000, splash.close)
    QTimer.singleShot(3000, win.show)

    sys.excepthook = except_hook
    sys.exit(app.exec())
