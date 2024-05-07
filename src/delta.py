import pprint


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


def harmful_action(cost_matrix: list[list[int]], sparse_matrix: list[list[int]], item_cors: list[int]):
    cost_item = cost_matrix[item_cors[0]][item_cors[1]]

    for item_index in range(len(sparse_matrix[item_cors[0]])):
        sparse_matrix[item_cors[0]][item_index] += cost_item

    return sparse_matrix


def useful_action(cost_matrix: list[list[int]], sparse_matrix: list[list[int]], item_cors: list[int]):
    cost_item = cost_matrix[item_cors[0]][item_cors[1]]

    for item_index in range(len(sparse_matrix)):
        sparse_matrix[item_index][item_cors[1]] -= cost_item

    return sparse_matrix


def delta_calculation(cost_matrix: list[list[int]], supply: list[int], demand: list[int], item_cors: list[int]):
    item_value = cost_matrix[item_cors[0]][item_cors[1]]
    supply_vector = create_zero_vector(len(supply), item_cors[0], item_value)
    shop_vector = create_zero_vector(len(demand), item_cors[1], item_value)
    delta = vectors_multiplication(shop_vector, demand) - vectors_multiplication(supply_vector, supply)
    return delta


def create_zero_vector(len_vector: int, item_position: int, item_value: int) -> list[int]:
    vector = [0 for _ in range(len_vector)]
    vector[item_position] = item_value
    return vector


def vectors_multiplication(first_vector: list[int], second_vector: list[int]) -> int:
    return sum(x * y for x, y in zip(first_vector, second_vector))


def delta_method(cost_matrix: list[list[int]], supply: list[int], demand: list[int]):
    sparse_matrix = matrix_dilution(cost_matrix)

    zero_cors = find_only_zero_items(sparse_matrix, cost_matrix)

    while not zero_cors:
        zero_cors = find_only_zero_items(sparse_matrix, cost_matrix)

    sparse_matrix = paired_transformation(zero_cors, sparse_matrix, cost_matrix, supply, demand)



def paired_transformation(zero_cors: list[int], sparse_matrix: list[list[int]], cost_matrix: list[list[int]],
                          supply: list[int], demand: list[int]):
    resp_sparse_matrix = [e.copy() for e in sparse_matrix]
    resp_sparse_matrix = harmful_action(cost_matrix, resp_sparse_matrix, zero_cors)
    resp_sparse_matrix = useful_action(cost_matrix, resp_sparse_matrix, zero_cors)
    delta = delta_calculation(cost_matrix, supply, demand, zero_cors)

    if delta == 0:
        return resp_sparse_matrix

    if delta > 0:
        resp_sparse_matrix = paired_transformation(zero_cors, resp_sparse_matrix, cost_matrix, supply, demand)
        return resp_sparse_matrix

    return sparse_matrix


def matrix_dilution(cost_matrix: list[list[int]]) -> list[list[int]]:
    sparse_matrix = []

    for row in cost_matrix:
        min_unit = min(row)
        sparse_matrix.append([item - min_unit for item in row])

    for column_index in range(len(sparse_matrix[0])):
        min_unit = min([item[column_index] for item in sparse_matrix])
        for item in sparse_matrix:
            item[column_index] -= min_unit

    return sparse_matrix
