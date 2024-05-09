from PyQt5 import uic
from PyQt5.QtWidgets import QSplashScreen, QDesktopWidget


class SplashScreen(QSplashScreen):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/SplashScreen.ui", self)
        self.center_on_screen()

    def center_on_screen(self):
        screen = QDesktopWidget().availableGeometry()
        self.move((screen.width() - self.width()) // 2, (screen.height() - self.height()) // 2)
