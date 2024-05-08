import random

from PyQt5 import uic
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import QMainWindow, QSpinBox, QLabel, QSizePolicy, QMessageBox

from SpinWidget import SpinWidget
from ThreadDeltaCalculate import ThreadDeltaCalculate

MATRIX = [
    [6, 5, 8, 7, 14],
    [3, 6, 4, 2, 12],
    [9, 1, 3, 6, 8],
    [10, 14, 6, 4]
]


class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.worker = None
        self.shops = None
        self.storages = None
        self.cost_matrix = None
        uic.loadUi('ui/MainWin.ui', self)
        self.shop_counter.valueChanged.connect(self.update_table)
        self.suppliers_counter.valueChanged.connect(self.update_table)
        self.pushButton.clicked.connect(self.extract_data)
        QTimer.singleShot(100, self.update_table)

    def extract_cost_matrix(self):
        cost_matrix = []
        for row in range(self.suppliers_counter.value()):
            row_data = []
            for column in range(self.shop_counter.value()):
                spin_box = self.tableWidget.cellWidget(row, column)
                row_data.append(spin_box.value())
            cost_matrix.append(row_data)
        return cost_matrix

    def extract_storages(self):
        storages = []
        for row in range(self.suppliers_counter.value()):
            spin_box = self.tableWidget.cellWidget(row, self.shop_counter.value())
            if type(spin_box) is SpinWidget:
                storages.append(spin_box.value())
                label = QLabel()
                label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
                label.setText(str(spin_box.value()))
                self.tableWidget_2.setCellWidget(row, self.suppliers_counter.value() + 1, label)
        return storages

    def extract_shops(self):
        shops = []
        for column in range(self.shop_counter.value()):
            spin_box = self.tableWidget.cellWidget(self.suppliers_counter.value(), column)
            if type(spin_box) is SpinWidget:
                shops.append(spin_box.value())
                label = QLabel()
                label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
                label.setText(str(spin_box.value()))
                self.tableWidget_2.setCellWidget(self.suppliers_counter.value(), column, label)
        return shops

    def extract_data(self):
        self.cost_matrix = self.extract_cost_matrix()
        self.storages = self.extract_storages()
        self.shops = self.extract_shops()
        self.calculate()

    def calculate(self):
        try:
            self.worker = ThreadDeltaCalculate(self.cost_matrix, self.storages, self.shops)
            self.worker.finished.connect(self.output_results)
            self.worker.start()
        except RecursionError:
            QMessageBox.warning(self, 'Решений нет',
                                'Предоставленный набор данных не имеет решений дельта-методом')

    def output_results(self, calculate_result):
        transportation_plan, result_sum = calculate_result
        label = QLabel()
        label.setText(str(result_sum))
        self.tableWidget_2.setCellWidget(self.suppliers_counter.value() + 1, 0, label)

        for row_index in range(len(transportation_plan)):
            for column_index in range(len(transportation_plan[row_index])):
                label = QLabel()
                value = transportation_plan[row_index][column_index]
                label.setText(str(value) if value != 0 else '')
                label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
                self.tableWidget_2.setCellWidget(row_index, column_index, label)

    def update_table(self):
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)

        self.tableWidget.setColumnCount(self.shop_counter.value() + 1)
        self.tableWidget.setRowCount(self.suppliers_counter.value() + 1)

        self.tableWidget_2.setColumnCount(self.shop_counter.value() + 1)
        self.tableWidget_2.setRowCount(self.suppliers_counter.value() + 2)

        suppliers_headers = []
        for supplier in range(1, self.shop_counter.value() + 1):
            suppliers_headers.append(f'Магазин {str(supplier)}')

        shop_headers = []
        for supplier in range(1, self.suppliers_counter.value() + 1):
            shop_headers.append(f'Поставщик {str(supplier)}')

        for row in range(self.tableWidget.rowCount()):
            for column in range(self.tableWidget.columnCount()):
                if type(self.tableWidget.cellWidget(row, column)) != QSpinBox and not (
                        row == self.tableWidget.rowCount() - 1 and column == self.tableWidget.columnCount() - 1
                ):
                    spin_box = SpinWidget()
                    spin_box.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                    spin_box.set_value(random.randint(1, 30))
                    spin_box.set_value(MATRIX[row][column])
                    self.tableWidget.setCellWidget(row, column, spin_box)
                elif row == self.tableWidget.rowCount() - 1 and column == self.tableWidget.columnCount() - 1:
                    label = QLabel(self)
                    self.tableWidget.setCellWidget(row, column, label)

        self.tableWidget.setHorizontalHeaderLabels(suppliers_headers + ['Запасы'])
        self.tableWidget.setVerticalHeaderLabels(shop_headers + ['Потребности'])

        self.tableWidget_2.setHorizontalHeaderLabels(suppliers_headers + ['Запасы'])
        self.tableWidget_2.setVerticalHeaderLabels(shop_headers + ['Потребности', 'Итог'])

        self.resize_cell_table()

    def resizeEvent(self, a0, QResizeEvent=None):
        self.resize_cell_table()

    def resize_cell_table(self):
        width = max(150, (self.tableWidget.width() - 150) // (self.shop_counter.value() + 1))
        height = max(50, (self.tableWidget.height() - 30) // (self.suppliers_counter.value() + 1))

        for row in range(self.tableWidget.rowCount()):
            self.tableWidget.setRowHeight(row, height)
            self.tableWidget_2.setRowHeight(row, height)

        height = max(60, (self.tableWidget.height() - 10) // (self.suppliers_counter.value() + 1))
        self.tableWidget_2.setRowHeight(self.tableWidget.rowCount(), height)
        self.tableWidget_2.setSpan(self.tableWidget.rowCount(), 0, self.tableWidget.rowCount(),
                                   self.tableWidget.columnCount())

        for column in range(self.tableWidget.columnCount()):
            self.tableWidget.setColumnWidth(column, width)
            self.tableWidget_2.setColumnWidth(column, width)
