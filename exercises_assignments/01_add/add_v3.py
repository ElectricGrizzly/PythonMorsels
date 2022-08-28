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
    # Ensure we have two matrices to add
    if len(matrices) == 1:
        return matrices[0]

    rows = len(matrices[0])
    columns = len(matrices[0][0])

    # Ensure matrices are of the same dimension to add element-wise
    for matrix in matrices:
        if len(matrix) != rows:
            raise ValueError('Given matrices are not the same size.')
        for row in matrix:
            if len(row) != columns:
                raise ValueError('Given matrices are not the same size.')
    del rows, columns

    # Add the 0th matrix to the 1st matrix
    for row_num, row in enumerate(matrices[0]):
        for col_num, element in enumerate(row):
            matrices[1][row_num][col_num] += element

    # If more than one matrix left, remove 0th matrix and add again, else return the final matrix
    if len(matrices) > 1:
        return add(*matrices[1:])      
    return matrices[0]
