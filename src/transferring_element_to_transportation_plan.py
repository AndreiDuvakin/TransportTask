from src.delete_line_from_matrix import delete_column_from_matrix, delete_row_from_matrix

FIRST_INDEX = 0
SECOND_INDEX = 1


class TransferringElementToPlan:
    def __init__(
            self, sparse_matrix: list[list[int]],
            cost_matrix: list[list[int]],
            transportation_plan: list[list[int]],
            storages: list[int],
            shops: list[int],
            item_cors: list[int]
    ):
        self.sparse_matrix = sparse_matrix
        self.cost_matrix = cost_matrix
        self.transportation_plan = transportation_plan
        self.storages = storages
        self.shops = shops
        self.item_cors = item_cors
        self.storages_item = storages[item_cors[FIRST_INDEX]]
        self.shops_item = shops[item_cors[SECOND_INDEX]]

    def calculate(self):
        self.comparing_items()
        return self.sparse_matrix, self.cost_matrix, self.transportation_plan, self.storages, self.shops

    def comparing_items(self):
        if self.shops_item > self.storages_item:
            self.transfer_storage_to_plan()
        elif self.shops_item == self.storages_item:
            self.transfer_shop_and_storage_to_plan()
        else:
            self.transfer_shop_to_plan()

    def transfer_storage_to_plan(self):
        self.transportation_plan[self.item_cors[FIRST_INDEX]][self.item_cors[SECOND_INDEX]] = self.storages_item
        self.shops[self.item_cors[SECOND_INDEX]] -= self.storages_item
        del self.storages[self.item_cors[FIRST_INDEX]]

        self.sparse_matrix = delete_row_from_matrix(self.sparse_matrix, self.item_cors[FIRST_INDEX])
        self.cost_matrix = delete_row_from_matrix(self.cost_matrix, self.item_cors[FIRST_INDEX])

    def transfer_shop_and_storage_to_plan(self):
        self.transportation_plan[self.item_cors[FIRST_INDEX]][self.item_cors[SECOND_INDEX]] = self.storages_item
        del self.storages[self.item_cors[FIRST_INDEX]]
        del self.shops[self.item_cors[SECOND_INDEX]]

        self.sparse_matrix = delete_column_from_matrix(self.sparse_matrix, self.item_cors[FIRST_INDEX])
        self.sparse_matrix = delete_row_from_matrix(self.sparse_matrix, self.item_cors[SECOND_INDEX])

        self.cost_matrix = delete_column_from_matrix(self.cost_matrix, self.item_cors[FIRST_INDEX])
        self.cost_matrix = delete_row_from_matrix(self.cost_matrix, self.item_cors[SECOND_INDEX])

    def transfer_shop_to_plan(self):
        self.transportation_plan[self.item_cors[FIRST_INDEX]][self.item_cors[SECOND_INDEX]] = self.shops_item
        del self.shops[self.item_cors[SECOND_INDEX]]
        self.storages[self.item_cors[FIRST_INDEX]] -= self.shops_item

        self.sparse_matrix = delete_column_from_matrix(self.sparse_matrix, self.item_cors[SECOND_INDEX])
        self.cost_matrix = delete_column_from_matrix(self.cost_matrix, self.item_cors[SECOND_INDEX])
