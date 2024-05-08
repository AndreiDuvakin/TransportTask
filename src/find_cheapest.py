def find_cheapest(matrix: list[list[int]]) -> list[int]:
    cheapest = [0, 0]

    for row_index in range(len(matrix)):
        for item_index in range(len(matrix[row_index])):
            if matrix[row_index][item_index] < matrix[cheapest[0]][cheapest[1]]:
                cheapest = [row_index, item_index]

    return cheapest
