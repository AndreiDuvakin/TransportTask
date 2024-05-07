import sys

from PyQt5 import uic
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/MainWin.ui', self)
        self.spinBox.valueChanged.connect(self.update_table)
        self.spinBox_3.valueChanged.connect(self.update_table)
        QTimer.singleShot(100, self.update_table)

    def update_table(self):
        self.tableWidget.setColumnCount(self.spinBox.value() + 1)
        self.tableWidget.setRowCount(self.spinBox_3.value() + 1)

        suppliers_headers = []
        for supplier in range(1, self.spinBox.value() + 1):
            suppliers_headers.append(f'Поставщик {str(supplier)}')

        shop_headers = []
        for supplier in range(1, self.spinBox_3.value() + 1):
            shop_headers.append(f'Магазин {str(supplier)}')

        self.tableWidget.setHorizontalHeaderLabels(suppliers_headers + ['Запасы'])
        self.tableWidget.setVerticalHeaderLabels(shop_headers + ['Потребности'])

        self.resize_cell_table()

    def resizeEvent(self, a0, QResizeEvent=None):
        self.resize_cell_table()

    def resize_cell_table(self):
        width = max(150, (self.tableWidget.width() - 150) // (self.spinBox.value() + 1))
        height = max(50, (self.tableWidget.height() - 30) // (self.spinBox_3.value() + 1))

        for row in range(self.tableWidget.rowCount()):
            self.tableWidget.setRowHeight(row, height)

        for column in range(self.tableWidget.columnCount()):
            self.tableWidget.setColumnWidth(column, width)


def except_hook(a, b, c):
    sys.__excepthook__(a, b, c)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
