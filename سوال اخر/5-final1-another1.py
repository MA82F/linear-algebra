import numpy as np



key_matrix = []

def get_submatrix00(key_matrix, row, col,n):
    """
    Generate a submatrix by removing the specified row and column.
    """
    return [r[:col] + r[col+1:] for r in (key_matrix[:row] + key_matrix[row+1:])]

def get_submatrix0n(key_matrix, row, col,n):
    """
    Generate a submatrix by removing the specified row and column.
    """
    return [r[:n-1] + r[n:] for r in (key_matrix[:row] + key_matrix[row+1:])]

def get_submatrixn0(key_matrix, row, col,n):
    """
    Generate a submatrix by removing the specified row and column.
    """
    return [r[:col-2] + r[col-1:] for r in (key_matrix[:n-1] + key_matrix[n:])]

def get_submatrixnn(key_matrix, row, col,n):
    """
    Generate a submatrix by removing the specified row and column.
    """
    return [r[:n-1] + r[n:] for r in (key_matrix[:n-1] + key_matrix[n:])]
def get_submatrix00nn(key_matrix, row, col,n):
    """
    Generate a submatrix by removing the specified row and column.
    """
    sub00 = [r[:col] + r[col+1:] for r in (key_matrix[:row] + key_matrix[row+1:])]
    sub00nn = [r[:n-1] + r[n:] for r in (sub00[:n-1] + sub00[n:])]
    return sub00nn



def get_key_matrix():
    n = int(input())
    for i in range(n):
        line = input()
        key_matrix.append(list(map(float, line.split())))

def calculate_determinant(matrix):
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
            sub_det0 = calculate_determinant(submatrix)
            #det += matrix[0][col] * sub_det
        elif(col == 1):
            submatrix = get_submatrix0n(matrix, 0, col,n)
            sub_det1 = calculate_determinant(submatrix)
            #det += matrix[0][col] * sub_det
        elif(col == 2):
            submatrix = get_submatrixn0(matrix, 0, col,n)
            sub_det2 = calculate_determinant(submatrix)
           # det += matrix[0][col] * sub_det
        elif(col == 3):
            submatrix = get_submatrixnn(matrix, 0, col,n)
            sub_det3 = calculate_determinant(submatrix)
           # det += matrix[0][col] * sub_det
    #matrixtemp = []
    submatrixtemp = []
    return (sub_det0 * sub_det3 - sub_det1 * sub_det2)*(1/calculate_determinant(get_submatrix00nn(matrix, 0, 0,n-1)))
    #return det

def determinant():
    get_key_matrix()
    if key_matrix is not None:
        determinant = calculate_determinant(key_matrix)
        if determinant == 0:
            print("NO_VALID_KEY")
            exit
        else:
            return f"{determinant:.2f}"


# Assuming key_matrix and text_matrix are defined and are lists of lists
def matrix_multiplication_mod_26(A, B):
    result = [[0] * len(B[0]) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            sum = 0
            for k in range(len(B)):
                sum += A[i][k] * B[k][j]
            result[i][j] = sum % 26
    return result


def hill_cipher_encrypt(text, key_matrix):
    """
    Encrypt the given text using the Hill cipher and the provided key matrix.
    """
    n = len(key_matrix)
    text = text.replace(" ", "_").upper()
    
    # Make sure the text length is a multiple of the key matrix size
    while len(text) % n != 0:
        text += '_'
    
    # Convert the text to numbers (A=0, B=1, ..., Z=25)
    text_vector = []
    for char in text:
        if char == '_':
            value = 27
        else:
            value = ord(char) - ord('A')
        text_vector.append(value)

   # text_vector = [ord(char) - ord('A') for char in text ]
    
    # Reshape text vector into a matrix form
    text_matrix = []
    for i in range(n):
        row = text_vector[i::n]
        text_matrix.append(row)
    # Transpose the matrix
    text_matrix = list(map(list, zip(*text_matrix)))
    
    # Encrypt the text
    encrypted_matrix = matrix_multiplication_mod_26(key_matrix, text_matrix)
    encrypted_vector = encrypted_matrix.T.flatten()
    
    # Convert numbers back to text
    encrypted_text = ''.join(chr(int(num) + ord('A')) for num in encrypted_vector)
    
    return encrypted_text








det = determinant()
text = input()
text = text.upper()
encrypted_text  = hill_cipher_encrypt(text,key_matrix)
print (encrypted_text)






def hill_cipher_encrypt(plain_text, key_matrix):
    n = key_matrix.shape[0]
    plain_text = plain_text.upper()
    padding_length = (n - len(plain_text) % n) % n
    plain_text += 'X' * padding_length
    encrypted_text = ""
    for i in range(0, len(plain_text), n):
        vector = [ord(char) - ord('A') for char in plain_text[i:i + n]]
        encrypted_vector = np.dot(key_matrix, vector) % 26
        encrypted_text += ''.join(chr(num + ord('A')) for num in encrypted_vector)
    return encrypted_text






def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return 1


def hill_cipher_decrypt(encrypted_text, key_matrix):
    n = key_matrix.shape[0]
    det = int(np.round(np.linalg.det(key_matrix)))
    det_inv = mod_inverse(det, 26)
    key_matrix_inv = det_inv * np.round(det * np.linalg.inv(key_matrix)).astype(int) % 26
    decrypted_text = ""
    for i in range(0, len(encrypted_text), n):
        vector = [ord(char) - ord('A') for char in encrypted_text[i:i + n]]
        decrypted_vector = np.dot(key_matrix_inv, vector) % 26
        decrypted_text += ''.join(chr(int(num) + ord('A')) for num in decrypted_vector)
    return decrypted_text

# مثال:
