from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class SpinWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/SpinWidget.ui', self)

    def set_value(self, value: int) -> None:
        self.spinBox.setValue(value)

    def value(self) -> int:
        return self.spinBox.value()
