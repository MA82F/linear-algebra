def calculate_determinant(matrix):
    n = len(matrix)
    det = 1
    sign = 1

    for i in range(n):
        # Find the pivot
        pivot = i
        for j in range(i + 1, n):
            if abs(matrix[j][i]) > abs(matrix[pivot][i]):
                pivot = j
        
        # Swap rows if necessary
        if i != pivot:
            matrix[i], matrix[pivot] = matrix[pivot], matrix[i]
            sign *= -1
        
        # If the pivot is zero, the determinant is zero
        if matrix[i][i] == 0:
            return 0
        
        # Eliminate below
        for j in range(i + 1, n):
            factor = matrix[j][i] / matrix[i][i]
            for k in range(i, n):
                matrix[j][k] -= factor * matrix[i][k]
    
    # Compute the determinant
    for i in range(n):
        det *= matrix[i][i]

    return det * sign

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [0, 8, 9]
]

determinant = calculate_determinant(matrix)
print("Determinant:", determinant)
