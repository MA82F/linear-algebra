matrix = []

def get_matrix_input():
    global matrix
    n = int(input())
    for i in range(n):
        line = input()
        matrix.append(list(map(float, line.split())))

def calculate_determinant(matrix, memo):
    matrix_tuple = tuple(map(tuple, matrix))
    if matrix_tuple in memo:
        return memo[matrix_tuple]
    
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        memo[matrix_tuple] = determinant
        return determinant
    else:
        determinant = 0
        for c in range(n):
            if matrix[0][c] == 0:
                continue
            sub_matrix = [row[:c] + row[c+1:] for row in matrix[1:]]
            determinant += ((-1) ** c) * matrix[0][c] * calculate_determinant(sub_matrix, memo)
        memo[matrix_tuple] = determinant
        return determinant

get_matrix_input()
memo = {}
determinant = calculate_determinant(matrix, memo)
print(int(determinant))
