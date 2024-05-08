def delete_row_from_matrix(matrix: list[list[int]], row_index: int) -> list[list[int]]:
    del matrix[row_index]
    return matrix


def delete_column_from_matrix(matrix: list[list[int]], column_index: int) -> list[list[int]]:
    for row in range(len(matrix)):
        del matrix[row][column_index]

    return matrix
