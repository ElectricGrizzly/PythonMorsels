'''
Add together any number of matrices and provide a positional sum matrix.

Written for Python Morsels Exercise/Assignment #1 "add"

Functions:

    add(*matrices: list[list[int|float]]) -> list[list[int|float]
    - Returns a matrix (list of lists) of given matrix values added positionally.
'''

def add(*matrices: list[list[int|float]]) -> list[list[int|float]]:
    '''
    Returns a matrix (list of lists) of given matrix values added positionally.

    Parameters:
        *matrices (list[list[int|float]]): Any number of matrices to add together positionally.

    Returns:
        total_matrix (list[list[int|float]]): A matrix of positional totals from given matrices. 
    '''
    outer_length: int = len(matrices[0])
    inner_length: int = len(matrices[0][0])
    for matrix in matrices:
        if len(matrix) != outer_length:
            raise ValueError('Given matrices are not the same size.')
        for row in matrix:
            if len(row) != inner_length:
                raise ValueError('Given matrices are not the same size.')

    matrices: zip = zip(*matrices)
    total_matrix: list[list[int]] = []
    for matrix in matrices:
        matrix_row: list[int] = []
        for row in zip(*matrix):
            row_total: int = 0
            for number in row:
                row_total += number
            matrix_row.append(row_total)
        total_matrix.append(matrix_row)
    return total_matrix
