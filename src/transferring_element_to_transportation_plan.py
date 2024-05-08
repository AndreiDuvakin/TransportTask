from src.delete_line_from_matrix import delete_column_from_matrix, delete_row_from_matrix


def transferring_element_to_transportation_plan(sparse_matrix: list[list[int]], cost_matrix: list[list[int]],
                                                transportation_plan: list[list[int]],
                                                storages: list[int], shops: list[int], item_cors: list[int]) -> (
        list[list[int]], list[list[int]], list[list[int]], list[int], list[int]
):
    storages_item = storages[item_cors[0]]
    shops_item = shops[item_cors[1]]

    if shops_item > storages_item:
        transportation_plan[item_cors[0]][item_cors[1]] = storages_item
        shops[item_cors[1]] -= storages_item
        del storages[item_cors[0]]

        sparse_matrix = delete_row_from_matrix(sparse_matrix, item_cors[0])
        cost_matrix = delete_row_from_matrix(cost_matrix, item_cors[0])

    elif shops_item == storages_item:
        transportation_plan[item_cors[0]][item_cors[1]] = storages_item
        del storages[item_cors[0]]
        del shops[item_cors[1]]

        sparse_matrix = delete_column_from_matrix(sparse_matrix, item_cors[0])
        sparse_matrix = delete_row_from_matrix(sparse_matrix, item_cors[1])

        cost_matrix = delete_column_from_matrix(cost_matrix, item_cors[0])
        cost_matrix = delete_row_from_matrix(cost_matrix, item_cors[1])

    else:
        transportation_plan[item_cors[0]][item_cors[1]] = shops_item
        del shops[item_cors[1]]
        storages[item_cors[0]] -= shops_item

        sparse_matrix = delete_column_from_matrix(sparse_matrix, item_cors[1])
        cost_matrix = delete_column_from_matrix(cost_matrix, item_cors[1])

    return sparse_matrix, cost_matrix, transportation_plan, storages, shops
