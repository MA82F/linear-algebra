
matrix = []
divisionbyzeroflag = False

def get_submatrix00(matrix,n):
    return [r[:0] + r[1:] for r in (matrix[:0] + matrix[1:])]

def get_submatrix0n(matrix,n):
    return [r[:n-1] + r[n:] for r in (matrix[:0] + matrix[1:])]

def get_submatrixn0(matrix, n):
    return [r[:0] + r[1:] for r in (matrix[:n-1] + matrix[n:])]

def get_submatrixnn(matrix,n):
    return [r[:n-1] + r[n:] for r in (matrix[:n-1] + matrix[n:])]
def get_submatrix00nn(matrix, n):
    sub00 = [r[:0] + r[1:] for r in (matrix[:0] + matrix[1:])]
    sub00nn = [r[:n-1] + r[n:] for r in (sub00[:n-1] + sub00[n:])]
    return sub00nn



def get_matrix_input():
    n = int(input())
    for i in range(n):
        line = input()
        matrix.append(list(map(float, line.split())))

def calculate_determinant(matrix):
    """
    Calculate the determinant of an n x n matrix using the given algorithm.
    """
    global divisionbyzeroflag
    if divisionbyzeroflag:
        return 0
    n = len(matrix)
    
    # Base case for a 1x1 matrix
    if n == 1:
        return matrix[0][0]
    
    # Base case for a 2x2 matrix
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    # Recursive case for larger matrices
    sub_det0=0
    sub_det1=0
    sub_det2=0
    sub_det3=0
    submatrix = get_submatrix00(matrix,n)
    sub_det0 = calculate_determinant(submatrix)
    #det += matrix[0][col] * sub_det

    submatrix = get_submatrix0n(matrix,n)
    sub_det1 = calculate_determinant(submatrix)

    submatrix = get_submatrixn0(matrix,n)
    sub_det2 = calculate_determinant(submatrix)

    submatrix = get_submatrixnn(matrix,n)
    sub_det3 = calculate_determinant(submatrix)

    submat = get_submatrix00nn(matrix,n-1)

    divisionbyzero = calculate_determinant(submat)
    if divisionbyzero == 0:
        divisionbyzeroflag = True
        return 0
        return "divisionbyzero"
        submat[1], submat[2] = submat[2], submat[1]
        divisionbyzero = calculate_determinant(submat)
    return ((sub_det0 * sub_det3) - (sub_det1 * sub_det2))*(1/divisionbyzero)
    #return det

get_matrix_input()

determinant = calculate_determinant(matrix)
if divisionbyzeroflag :
    matrix[0], matrix[1] = matrix[1], matrix[0]
    divisionbyzeroflag = False
    determinant = - calculate_determinant(matrix)
for i in range(len(matrix)-1):
    if divisionbyzeroflag :
        matrix[i], matrix[i+1] = matrix[i+1], matrix[i]
        divisionbyzeroflag = False
        if i%2 == 1:
            determinant = - calculate_determinant(matrix)
        else:
            determinant = calculate_determinant(matrix)
    else:
        break
if divisionbyzeroflag :
    determinant = 0
if determinant == -0.00:
    determinant = 0
print(int(determinant))