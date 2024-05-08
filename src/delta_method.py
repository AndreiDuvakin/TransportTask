from src.copy_list import copy_int_vector, copy_int_matrix
from src.create_zero_list import create_zero_matrix
from src.find_cheapest import find_cheapest
from src.find_only_zero_items import find_only_zero_items
from src.matrix_dilution import matrix_dilution
from src.paired_transformation import paired_transformation
from src.transferring_element_to_transportation_plan import TransferringElementToPlan


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

    plan = TransferringElementToPlan(
        sparse_matrix, cost_matrix_copy, transportation_plan, storages_copy, shops_copy, zero_cors
    )
    plan.calculate()

    cheapest_cors = find_cheapest(plan.cost_matrix)
    plan.set_new_item_cors(cheapest_cors)
    plan.calculate()

    while zero_cors and plan.storages and plan.shops and plan.sparse_matrix:
        zero_cors = find_only_zero_items(plan.sparse_matrix, plan.cost_matrix)
        plan.set_new_item_cors(zero_cors)
        plan.calculate()

    result_summ = sum(
        [
            plan.transportation_plan[row_index][column_index] * cost_matrix[row_index][column_index] for row_index in
            range(len(plan.transportation_plan)) for column_index in range(len(plan.transportation_plan[row_index]))
        ]
    )

    return plan.transportation_plan, result_summ
