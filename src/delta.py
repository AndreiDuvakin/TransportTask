from src.copy_list import copy_int_vector, copy_int_matrix
from src.create_zero_list import create_zero_matrix
from src.find_cheapest import find_cheapest
from src.find_only_zero_items import find_only_zero_items
from src.matrix_dilution import matrix_dilution
from src.paired_transformation import paired_transformation
from src.transferring_element_to_transportation_plan import transferring_element_to_transportation_plan


def delta_method(cost_matrix: list[list[int]], storages: list[int], shops: list[int]):
    sparse_matrix = matrix_dilution(cost_matrix)

    zero_cors = find_only_zero_items(sparse_matrix, cost_matrix)

    while not zero_cors:
        zero_cors = find_only_zero_items(sparse_matrix, cost_matrix)

    sparse_matrix = paired_transformation(zero_cors, sparse_matrix, cost_matrix, storages, shops)
    transportation_plan = create_zero_matrix(len(shops), len(storages))

    storages_copy = copy_int_vector(storages)
    shops_copy = copy_int_vector(shops)
    cost_matrix_copy = copy_int_matrix(cost_matrix)

    sparse_matrix, cost_matrix_copy, transportation_plan, storages_copy, shops_copy = (
        transferring_element_to_transportation_plan(
            sparse_matrix, cost_matrix_copy, transportation_plan, storages_copy, shops_copy, zero_cors
        )
    )

    cheapest_cors = find_cheapest(cost_matrix_copy)

    sparse_matrix, cost_matrix_copy, transportation_plan, storages_copy, shops_copy = (
        transferring_element_to_transportation_plan(
            sparse_matrix, cost_matrix_copy, transportation_plan, storages_copy, shops_copy, cheapest_cors
        )
    )

    zero_cors = find_only_zero_items(sparse_matrix, cost_matrix_copy)

    while zero_cors and storages_copy and shops_copy:
        sparse_matrix, cost_matrix_copy, transportation_plan, storages_copy, shops_copy = (
            transferring_element_to_transportation_plan(
                sparse_matrix, cost_matrix_copy, transportation_plan, storages_copy, shops_copy, zero_cors
            )
        )

        if sparse_matrix:
            zero_cors = find_only_zero_items(sparse_matrix, cost_matrix_copy)

    result_summ = sum(
        [transportation_plan[row_index][column_index] * cost_matrix[row_index][column_index] for row_index in
         range(len(transportation_plan)) for column_index in range(len(transportation_plan[row_index]))]
    )

    return transportation_plan, result_summ
