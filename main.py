import random
import sys
from pprint import pprint

from PyQt5 import uic
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QSpinBox, QLabel, QWidget, QSizePolicy


class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/MainWin.ui', self)
        self.spinBox.valueChanged.connect(self.update_table)
        self.spinBox_3.valueChanged.connect(self.update_table)
        self.pushButton.clicked.connect(self.lest_math)
        QTimer.singleShot(100, self.update_table)

    def lest_math(self):
        cost_matrix = []
        for row in range(self.spinBox_3.value()):
            row_data = []
            for column in range(self.spinBox.value()):
                spin_box = self.tableWidget.cellWidget(row, column)
                row_data.append(spin_box.value())
            cost_matrix.append(row_data)

        supply = []
        for row in range(self.spinBox.value()):
            spin_box = self.tableWidget.cellWidget(row, self.spinBox.value())
            if type(spin_box) is QSpinBox:
                supply.append(spin_box.value())

        demand = []
        for column in range(self.spinBox_3.value()):
            spin_box = self.tableWidget.cellWidget(self.spinBox_3.value(), column)
            if type(spin_box) is QSpinBox:
                demand.append(spin_box.value())

    def update_table(self):
        self.tableWidget.setColumnCount(self.spinBox.value() + 1)
        self.tableWidget.setRowCount(self.spinBox_3.value() + 1)

        suppliers_headers = []
        for supplier in range(1, self.spinBox.value() + 1):
            suppliers_headers.append(f'Поставщик {str(supplier)}')

        shop_headers = []
        for supplier in range(1, self.spinBox_3.value() + 1):
            shop_headers.append(f'Магазин {str(supplier)}')

        for row in range(self.tableWidget.rowCount() + 1):
            for column in range(self.tableWidget.columnCount() + 1):
                if type(self.tableWidget.cellWidget(row, column)) != QSpinBox and not (
                        row == self.tableWidget.rowCount() - 1 and column == self.tableWidget.columnCount() - 1
                ):
                    spin_box = SpinWidget()
                    spin_box.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                    spin_box.setValue(random.randint(1, 30))
                    self.tableWidget.setCellWidget(row, column, spin_box)
                elif row == self.tableWidget.rowCount() - 1 and column == self.tableWidget.columnCount() - 1:
                    label = QLabel(self)
                    self.tableWidget.setCellWidget(row, column, label)

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


class SpinWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/SpinWidget.ui', self)

    def setValue(self, value: int):
        self.spinBox.setValue(value)

    def value(self):
        return self.spinBox.value()


def except_hook(a, b, c):
    sys.__excepthook__(a, b, c)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
