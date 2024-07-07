import tkinter as tk
from tkinter import messagebox

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

def get_submatrix00(matrix, row, col, n):
    return [r[:col] + r[col+1:] for r in (matrix[:row] + matrix[row+1:])]

def get_submatrix0n(matrix, row, col, n):
    return [r[:n-1] + r[n:] for r in (matrix[:row] + matrix[row+1:])]

def get_submatrixn0(matrix, row, col, n):
    return [r[:col-2] + r[col-1:] for r in (matrix[:n-1] + matrix[n:])]

def get_submatrixnn(matrix, row, col, n):
    return [r[:n-1] + r[n:] for r in (matrix[:n-1] + matrix[n:])]

def get_submatrix00nn(matrix, row, col, n):
    sub00 = [r[:col] + r[col+1:] for r in (matrix[:row] + matrix[row+1:])]
    sub00nn = [r[:n-1] + r[n:] for r in (sub00[:n-1] + sub00[n:])]
    return sub00nn

def calculate_determinant(matrix, divisionbyzeroflag):
    if divisionbyzeroflag:
        return 0
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    det = 0
    sub_det0 = 0
    sub_det1 = 0
    sub_det2 = 0
    sub_det3 = 0
    for col in range(n+1):
        if(col == 0):
            submatrix = get_submatrix00(matrix, 0, col, n)
            sub_det0 = calculate_determinant(submatrix, divisionbyzeroflag)
        elif(col == 1):
            submatrix = get_submatrix0n(matrix, 0, col, n)
            sub_det1 = calculate_determinant(submatrix, divisionbyzeroflag)
        elif(col == 2):
            submatrix = get_submatrixn0(matrix, 0, col, n)
            sub_det2 = calculate_determinant(submatrix, divisionbyzeroflag)
        elif(col == 3):
            submatrix = get_submatrixnn(matrix, 0, col, n)
            sub_det3 = calculate_determinant(submatrix, divisionbyzeroflag)
    
    submat = get_submatrix00nn(matrix, 0, 0, n-1)
    divisionbyzero = calculate_determinant(submat, divisionbyzeroflag)
    if divisionbyzero == 0:
        divisionbyzeroflag = True
        return 0
        return "divisionbyzero"
    submat[1], submat[2] = submat[2], submat[1]
    divisionbyzero = calculate_determinant(submat)
    return (sub_det0 * sub_det3 - sub_det1 * sub_det2) * (1 / divisionbyzero)

def is_invertible(matrix, n):
    det = calculate_determinant(matrix, divisionbyzeroflag)
    if divisionbyzeroflag:
        matrix[0], matrix[1] = matrix[1], matrix[0]
        det = calculate_determinant(matrix, divisionbyzeroflag=True)
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

def hill_cipher_encrypt(plaintext, key_matrix, n):
    plaintext_numbers = [char_to_num(c) for c in plaintext]
    while len(plaintext_numbers) % n != 0:
        plaintext_numbers.append(char_to_num('_'))

    encrypted_numbers = []
    for i in range(0, len(plaintext_numbers), n):
        chunk = plaintext_numbers[i:i + n]
        encrypted_chunk = [0] * n
        for row in range(n):
            encrypted_chunk[row] = sum(key_matrix[row][col] * chunk[col] for col in range(n)) % 27
        encrypted_numbers.extend(encrypted_chunk)

    encrypted_text = ''.join(num_to_char(num) for num in encrypted_numbers)
    return encrypted_text

def set_matrix_size():
    global matrix_entries
    n = int(matrix_size_entry.get())
    
    for entry in matrix_entries:
        entry.grid_forget()
    
    matrix_entries = []
    for i in range(n):
        row_entries = []
        for j in range(n):
            entry = tk.Entry(app, width=5)
            entry.grid(row=i+2, column=j)
            row_entries.append(entry)
        matrix_entries.append(row_entries)

def encrypt_text():
    global key_matrix
    key_matrix = []

    try:
        n = int(matrix_size_entry.get())
        for row_entries in matrix_entries:
            row = [int(entry.get()) for entry in row_entries]
            key_matrix.append(row)

        if not is_invertible(key_matrix, n):
            messagebox.showerror("Error", "NO_VALID_KEY")
            return

        plaintext = plaintext_entry.get().replace(' ', '_')
        encrypted_text = hill_cipher_encrypt(plaintext, key_matrix, n)
        result_label.config(text=f"Encrypted Text: {encrypted_text}")

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter integers only.")

app = tk.Tk()
app.title("Hill Cipher Encryption")

tk.Label(app, text="Matrix Size (n):").grid(row=0, column=0)
matrix_size_entry = tk.Entry(app)
matrix_size_entry.grid(row=0, column=1)

matrix_entries = []

set_size_button = tk.Button(app, text="Set Size", command=set_matrix_size)
set_size_button.grid(row=0, column=2)

tk.Label(app, text="Plaintext:").grid(row=1, column=0)
plaintext_entry = tk.Entry(app)
plaintext_entry.grid(row=1, column=1, columnspan=2)

encrypt_button = tk.Button(app, text="Encrypt", command=encrypt_text)
encrypt_button.grid(row=6, column=0, columnspan=3, pady=5)

result_label = tk.Label(app, text="")
result_label.grid(row=7, column=0, columnspan=3)

app.mainloop()
