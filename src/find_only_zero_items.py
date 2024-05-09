from src.constants import NEGATIVE_IMPOSSIBLE_VALUE, FIRST_INDEX, SECOND_INDEX
from src.replace_items_by_index import replace_item_by_index


class ProcessedSingleZero:
    def __init__(
            self,
            sparse_matrix: list[list[int]],
            cost_matrix: list[list[int]],
            ignoring_rows: list[int] = (),
            ignoring_columns: list[int] = ()
    ):
        self.sparse_matrix = sparse_matrix
        self.cost_matrix = cost_matrix
        self.ignoring_rows = ignoring_rows
        self.ignoring_columns = ignoring_columns
        self.zero_items_cors = []

    def replace_values_of_ignored_rows(self):
        for row_index in range(len(self.sparse_matrix)):
            self.sparse_matrix[row_index] = replace_item_by_index(self.sparse_matrix[row_index], self.ignoring_columns)

    def replace_values_of_ignored_column(self):
        num_rows = len(self.sparse_matrix)
        for column_index in self.ignoring_columns:
            for row_index in range(num_rows):
                self.sparse_matrix[row_index][column_index] = NEGATIVE_IMPOSSIBLE_VALUE

    def processing(self):
        self.replace_values_of_ignored_rows()
        self.replace_values_of_ignored_column()
        self.find_single_zero_rows()
        self.find_single_zero_columns()

        if not self.zero_items_cors:
            return []

        return self.select_cheapest()

    def find_single_zero_rows(self):
        for row_index in range(len(self.sparse_matrix)):
            if self.sparse_matrix[row_index].count(0) == 1 and row_index not in self.ignoring_rows:
                self.zero_items_cors.append([row_index, self.sparse_matrix[row_index].index(0)])

    def find_single_zero_columns(self):
        for column_index in range(len(self.sparse_matrix[FIRST_INDEX])):
            column = [item[column_index] for item in self.sparse_matrix]
            if column.count(0) == 1 and column_index not in self.ignoring_columns:
                self.zero_items_cors.append([column.index(0), column_index])

    def select_cheapest(self):
        response_zero_item = self.zero_items_cors[FIRST_INDEX]
        for zero_item in self.zero_items_cors:
            if (
                    self.cost_matrix[zero_item[FIRST_INDEX]][zero_item[SECOND_INDEX]] <
                    self.cost_matrix[response_zero_item[FIRST_INDEX]][response_zero_item[SECOND_INDEX]]
            ):
                response_zero_item = zero_item

        return response_zero_item


def find_only_zero_items(
        sparse_matrix: list[list[int]],
        cost_matrix: list[list[int]],
        ignoring_rows: list[int] = (),
        ignoring_columns: list[int] = ()
) -> list[int]:
    zero_items_cors = []

    for row_index in range(len(sparse_matrix)):
        checking_row = replace_item_by_index(sparse_matrix[row_index], ignoring_columns)
        if checking_row.count(0) == 1 and row_index not in ignoring_rows:
            zero_items_cors.append([row_index, sparse_matrix[row_index].index(0)])

    for column_index in range(len(sparse_matrix[0])):
        column = replace_item_by_index([item[column_index] for item in sparse_matrix], ignoring_rows)
        if column.count(0) == 1 and column_index not in ignoring_columns:
            zero_items_cors.append([column.index(0), column_index])

    if not zero_items_cors:
        return []

    response_zero_item = zero_items_cors[0]

    for zero_item in zero_items_cors:
        if cost_matrix[zero_item[0]][zero_item[1]] < cost_matrix[response_zero_item[0]][response_zero_item[1]]:
            response_zero_item = zero_item

    return response_zero_item
