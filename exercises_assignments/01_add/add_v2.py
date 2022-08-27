'''
Add together any number of matrices and provide a positional sum matrix.
Written for Python Morsels Exercise/Assignment #1 "add"
Functions:
    add(*matrices: list[list[int|float]]) -> list[list[int|float]
    - Returns a matrix (list of lists) of given matrix values added positionally.
'''
def add(*matrices):
    '''
    Returns a matrix (list of lists) of given matrix values added positionally.
    Parameters:
        *matrices (list[list[int|float]]): Any number of matrices to add together positionally.
    Returns:
        total_matrix (list[list[int|float]]): A matrix of positional totals from given matrices. 
    '''
    rows = len(matrices[0])
    columns = len(matrices[0][0])

    for matrix in matrices:
        if len(matrix) != rows:
            raise ValueError('Given matrices are not the same size.')
        for row in matrix:
            if len(row) != columns:
                raise ValueError('Given matrices are not the same size.')

    row = 0
    column = 0
    sum_matrix = []
    sum_row = []

    while (row < rows):
        
        total = 0
        for matrix in matrices:
            total += matrix[row][column]
            elements_visited += 1
        sum_row.append(total)

        column += 1
        if column == columns:
            sum_matrix.append(sum_row)
            sum_row = []
            column = 0
            row += 1
            
    return sum_matrix
