
matrix = []
matrix_array = []
matrix_determinant = []

def get_matrix_input():
    n = int(input())
    for i in range(n):
        line = input()
        matrix.append(list(map(float, line.split())))

def calculate_determinant(matrix):
    global matrix_array
    for i in range(len(matrix_array)):
        if [matrix] == matrix_array[i]:
            return matrix_determinant[i]
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        matrix_array.append([matrix])
        determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        matrix_determinant.append(determinant)
        return determinant
    else:
        determinant = 0
        for c in range(len(matrix)):
            if matrix[0][c] == 0:
                return 0
            else:
                determinant += ((-1) ** c) * matrix[0][c] * calculate_determinant([row[:c] + row[c+1:] for row in matrix[1:]])
        matrix_array.append([matrix])
        matrix_determinant.append(determinant)
        return determinant

get_matrix_input()
determinant = calculate_determinant(matrix)
print(int(determinant))
