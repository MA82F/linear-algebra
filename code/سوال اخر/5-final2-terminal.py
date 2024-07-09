def char_to_num(c):
    if c == '_':
        return 26
    return ord(c.upper()) - ord('A')

def num_to_char(n):
    if n == 26:
        return '_'
    return chr(n + ord('A'))

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


key_matrix = []


matrix = []
divisionbyzeroflag = False

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


def calculate_determinant(matrix,divisionbyzeroflag):
    """
    Calculate the determinant of an n x n matrix using the given algorithm.
    """
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
    det = 0
    sub_det0=0
    sub_det1=0
    sub_det2=0
    sub_det3=0
    for col in range(n+1):
        if(col == 0):
            submatrix = get_submatrix00(matrix, 0, col,n)
            sub_det0 = calculate_determinant(submatrix,divisionbyzeroflag)
            #det += matrix[0][col] * sub_det
        elif(col == 1):
            submatrix = get_submatrix0n(matrix, 0, col,n)
            sub_det1 = calculate_determinant(submatrix,divisionbyzeroflag)
            #det += matrix[0][col] * sub_det
        elif(col == 2):
            submatrix = get_submatrixn0(matrix, 0, col,n)
            sub_det2 = calculate_determinant(submatrix,divisionbyzeroflag)
           # det += matrix[0][col] * sub_det
        elif(col == 3):
            submatrix = get_submatrixnn(matrix, 0, col,n)
            sub_det3 = calculate_determinant(submatrix,divisionbyzeroflag)
           # det += matrix[0][col] * sub_det
    #matrixtemp = []
    submatrixtemp = []
    submat = get_submatrix00nn(matrix, 0, 0,n-1)
    divisionbyzero = calculate_determinant(submat,divisionbyzeroflag)
    if divisionbyzero == 0:
        divisionbyzeroflag = True
        return 0
        return "divisionbyzero"
        submat[1], submat[2] = submat[2], submat[1]
        divisionbyzero = calculate_determinant(submat)
    return (sub_det0 * sub_det3 - sub_det1 * sub_det2)*(1/divisionbyzero)
    #return det




def is_invertible(matrix, n):
    det = calculate_determinant(matrix,divisionbyzeroflag)
    if divisionbyzeroflag :
        matrix[0], matrix[1] = matrix[1], matrix[0]
        det = calculate_determinant(matrix,divisionbyzeroflag=True)
    det = det % 27
    return det != 0 and mod_inverse(det, 27) is not None

def matrix_mult(A, B, size):
    result = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] += A[i][k] * B[k][j]
            result[i][j] %= 27
    return result


def get_submatrix(matrix, row, col):
    """
    Generate a submatrix by removing the specified row and column.
    """
    return [r[:col] + r[col+1:] for r in (matrix[:row] + matrix[row+1:])]

def matrix_mod_inverse(matrix,divisionbyzeroflag, modulus):
    """
    Find the matrix inverse under modulo.
    """
    n = len(matrix)
    det = calculate_determinant(matrix,divisionbyzeroflag) % modulus
    inv_det = mod_inverse(det, modulus)
    
    if inv_det is None:
        return None
    
    adjugate_matrix = [[0] * n for _ in range(n)]
    for row in range(n):
        for col in range(n):
            minor = get_submatrix(matrix, row, col)
            det = calculate_determinant(minor,divisionbyzeroflag)
            if divisionbyzeroflag :
                matrix[0], matrix[1] = matrix[1], matrix[0]
                det = calculate_determinant(matrix,divisionbyzeroflag=True)
            cofactor = det * ((-1) ** (row + col))
            adjugate_matrix[col][row] = (cofactor * inv_det) % modulus
    divisionbyzeroflag = False
    return adjugate_matrix

def hill_cipher_decrypt(ciphertext,divisionbyzeroflag,key_matrix, n):
    ciphertext_numbers = [char_to_num(c) for c in ciphertext]
    
    inv_key_matrix = matrix_mod_inverse(key_matrix,divisionbyzeroflag, 27)
    if inv_key_matrix is None:
        return "NO_VALID_KEY"
    
    decrypted_numbers = []
    for i in range(0, len(ciphertext_numbers), n):
        chunk = ciphertext_numbers[i:i + n]
        decrypted_chunk = [0] * n
        for row in range(n):
            decrypted_chunk[row] = sum(inv_key_matrix[row][col] * chunk[col] for col in range(n)) % 27
        decrypted_numbers.extend(decrypted_chunk)
    
    decrypted_text = ''.join(num_to_char(num) for num in decrypted_numbers)
    return decrypted_text



n = int(input())
for _ in range(n):
    row = list(map(int, input().split()))
    key_matrix.append(row)
plaintext = input()

decrypted_text = hill_cipher_decrypt(plaintext,divisionbyzeroflag,key_matrix, n)
if decrypted_text[-1] == "_":
    decrypted_text = decrypted_text[:-1]
print(decrypted_text)
