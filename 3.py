def get_submatrix00(matrix, row, col,n):
    """
    Generate a submatrix by removing the specified row and column.
    """
    return [r[:col] + r[col+1:] for r in (matrix[:row] + matrix[row+1:])]

def get_submatrix0n(matrix, row, col,n):
    """
    Generate a submatrix by removing the specified row and column.
    """
    return [r[:n-1] + r[n:] for r in (matrix[:row] + matrix[row+1:])]

def get_submatrixn0(matrix, row, col,n):
    """
    Generate a submatrix by removing the specified row and column.
    """
    return [r[:col-2] + r[col-1:] for r in (matrix[:n-1] + matrix[n:])]

def get_submatrixnn(matrix, row, col,n):
    """
    Generate a submatrix by removing the specified row and column.
    """
    return [r[:n-1] + r[n:] for r in (matrix[:n-1] + matrix[n:])]
def get_submatrix00nn(matrix, row, col,n):
    """
    Generate a submatrix by removing the specified row and column.
    """
    sub00 = [r[:col] + r[col+1:] for r in (matrix[:row] + matrix[row+1:])]
    sub00nn = [r[:n-1] + r[n:] for r in (sub00[:n-1] + sub00[n:])]
    return sub00nn

def determinant(matrix):
    """
    Calculate the determinant of an n x n matrix using the given algorithm.
    """
    n = len(matrix)
    
    # Base case for a 1x1 matrix
    if n == 1:
        return matrix[0][0]
    
    # Base case for a 2x2 matrix
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    # Recursive case for larger matrices
    det = 0
    sub_det0=0
    sub_det1=0
    sub_det2=0
    sub_det3=0
    for col in range(n+1):
        if(col == 0):
            submatrix = get_submatrix00(matrix, 0, col,n)
            sub_det0 = determinant(submatrix)
            #det += matrix[0][col] * sub_det
        elif(col == 1):
            submatrix = get_submatrix0n(matrix, 0, col,n)
            sub_det1 = determinant(submatrix)
            #det += matrix[0][col] * sub_det
        elif(col == 2):
            submatrix = get_submatrixn0(matrix, 0, col,n)
            sub_det2 = determinant(submatrix)
           # det += matrix[0][col] * sub_det
        elif(col == 3):
            submatrix = get_submatrixnn(matrix, 0, col,n)
            sub_det3 = determinant(submatrix)
           # det += matrix[0][col] * sub_det
    #matrixtemp = []
    submatrixtemp = []
    return (sub_det0 * sub_det3 - sub_det1 * sub_det2)*(1/determinant(get_submatrix00nn(matrix, 0, 0,n-1)))
    #return det

# Example usage
matrix = [
    [1, 2, 3,4],
    [5, 6,7,8],
    [9,10,11,12],
    [13,14,15,16],
]

print(f"Determinant: {determinant(matrix)}")
