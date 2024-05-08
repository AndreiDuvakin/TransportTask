from PyQt5.QtCore import QThread, pyqtSignal

from src.delta_method import delta_method


class ThreadDeltaCalculate(QThread):
    finished = pyqtSignal(object)

    def __init__(self, cost_matrix, storages, shop):
        super().__init__()
        self.cost_matrix = cost_matrix
        self.storages = storages
        self.shop = shop

    def run(self):
        try:
            transportation_plan, result_sum = delta_method(self.cost_matrix, self.storages, self.shop)
            self.finished.emit((transportation_plan, result_sum))
        except RecursionError:
            self.finished.emit(None)
