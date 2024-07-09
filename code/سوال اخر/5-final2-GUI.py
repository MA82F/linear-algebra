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
divisionbyzeroflag = False

def get_submatrix(matrix, row, col):
    return [r[:col] + r[col+1:] for r in (matrix[:row] + matrix[row+1:])]

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

def matrix_mod_inverse(matrix, divisionbyzeroflag, modulus):
    n = len(matrix)
    det = calculate_determinant(matrix, divisionbyzeroflag) % modulus
    inv_det = mod_inverse(det, modulus)
    
    if inv_det is None:
        return None
    
    adjugate_matrix = [[0] * n for _ in range(n)]
    for row in range(n):
        for col in range(n):
            minor = get_submatrix(matrix, row, col)
            det = calculate_determinant(minor, divisionbyzeroflag)
            if divisionbyzeroflag:
                matrix[0], matrix[1] = matrix[1], matrix[0]
                det = calculate_determinant(matrix, divisionbyzeroflag=True)
            cofactor = det * ((-1) ** (row + col))
            adjugate_matrix[col][row] = (cofactor * inv_det) % modulus
    divisionbyzeroflag = False
    return adjugate_matrix

def hill_cipher_decrypt(ciphertext, divisionbyzeroflag, key_matrix, n):
    ciphertext_numbers = [char_to_num(c) for c in ciphertext]
    
    inv_key_matrix = matrix_mod_inverse(key_matrix, divisionbyzeroflag, 27)
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

def decrypt_text():
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

        ciphertext = ciphertext_entry.get().replace(' ', '_')
        decrypted_text = hill_cipher_decrypt(ciphertext, divisionbyzeroflag, key_matrix, n)
        result_label.config(text=f"Decrypted Text: {decrypted_text}")

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter integers only.")

app = tk.Tk()
app.title("Hill Cipher Decryption")

tk.Label(app, text="Matrix Size (n):").grid(row=0, column=0)
matrix_size_entry = tk.Entry(app)
matrix_size_entry.grid(row=0, column=1)

matrix_entries = []

set_size_button = tk.Button(app, text="Set Size", command=set_matrix_size)
set_size_button.grid(row=0, column=2)

tk.Label(app, text="Ciphertext:").grid(row=1, column=0)
ciphertext_entry = tk.Entry(app)
ciphertext_entry.grid(row=1, column=1, columnspan=2)

decrypt_button = tk.Button(app, text="Decrypt", command=decrypt_text)
decrypt_button.grid(row=6, column=0, columnspan=3, pady=5)

result_label = tk.Label(app, text="")
result_label.grid(row=7, column=0, columnspan=3)

app.mainloop()
