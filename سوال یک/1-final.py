
matrix = []

def get_matrix_input():
    n = int(input())
    for i in range(n):
        line = input()
        matrix.append(list(map(float, line.split())))

def calculate_determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        determinant = 0
        for c in range(len(matrix)):
            determinant += ((-1) ** c) * matrix[0][c] * calculate_determinant([row[:c] + row[c+1:] for row in matrix[1:]])
        return determinant

get_matrix_input()
if matrix is not None:
    determinant = calculate_determinant(matrix)
    print(f"{determinant:.2f}")
