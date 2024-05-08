from src.copy_list import copy_int_matrix
from src.delta_calculation import delta_calculation
from src.harmful_action import harmful_action
from src.useful_action import useful_action


def paired_transformation(zero_cors: list[int], sparse_matrix: list[list[int]], cost_matrix: list[list[int]],
                          storages: list[int], shops: list[int]):
    resp_sparse_matrix = copy_int_matrix(sparse_matrix)
    resp_sparse_matrix = harmful_action(cost_matrix, resp_sparse_matrix, zero_cors)
    resp_sparse_matrix = useful_action(cost_matrix, resp_sparse_matrix, zero_cors)
    delta = delta_calculation(cost_matrix, storages, shops, zero_cors)

    if delta == 0:
        return resp_sparse_matrix

    if delta > 0:
        resp_sparse_matrix = paired_transformation(zero_cors, resp_sparse_matrix, cost_matrix, storages, shops)
        return resp_sparse_matrix

    return sparse_matrix
