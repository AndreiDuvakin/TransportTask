def find_only_zero_items(sparse_matrix: list[list[int]], cost_matrix: list[list[int]]) -> list[int]:
    zero_items_cors = []

    for row_index in range(len(sparse_matrix)):
        if sparse_matrix[row_index].count(0) == 1:
            zero_items_cors.append([row_index, sparse_matrix[row_index].index(0)])

    for column_index in range(len(sparse_matrix[0])):
        column = [item[column_index] for item in sparse_matrix]
        if column.count(0) == 1:
            zero_items_cors.append([column.index(0), column_index])

    response_zero_item = zero_items_cors[0]

    for zero_item in zero_items_cors:
        if cost_matrix[zero_item[0]][zero_item[1]] < cost_matrix[response_zero_item[0]][response_zero_item[1]]:
            response_zero_item = zero_item

    return response_zero_item
