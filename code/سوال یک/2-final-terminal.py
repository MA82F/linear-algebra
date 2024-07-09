def get_matrix_input():
    matrix = []
    n = int(input())
    #print(f"Enter the {n}x{n} matrix row by row:")
    for i in range(n):
        line = input()
        matrix.append(list(map(float, line.split())))
    return matrix

def calculate_determinant(matrix):
    n = len(matrix)
    A = [row[:] for row in matrix]  # Make a copy of the matrix
    det = 1
    sign = 1

    for i in range(n):
        # Find the pivot
        pivot = i
        for j in range(i + 1, n):
            if abs(A[j][i]) > abs(A[pivot][i]):
                pivot = j
        
        # Swap rows if necessary
        if i != pivot:
            A[i], A[pivot] = A[pivot], A[i]
            sign *= -1
        
        # If the pivot is zero, the determinant is zero
        if A[i][i] == 0:
            return 0
        
        # Eliminate below
        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
    
    # Compute the determinant
    for i in range(n):
        det *= A[i][i]

    return det * sign

matrix = get_matrix_input()
if matrix:
    determinant = calculate_determinant(matrix)
    determinant = round(determinant, 2)
    if determinant == -0.0:
        determinant = 0.0
    print(int(determinant))
