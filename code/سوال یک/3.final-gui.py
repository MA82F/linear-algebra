import tkinter as tk
from tkinter import messagebox

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

def calculate_determinant(matrix):
    global divisionbyzeroflag
    if divisionbyzeroflag:
        return 0
    n = len(matrix)
    
    if n == 1:
        return matrix[0][0]
    
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    sub_det0 = 0
    sub_det1 = 0
    sub_det2 = 0
    sub_det3 = 0
    
    submatrix = get_submatrix00(matrix, n)
    sub_det0 = calculate_determinant(submatrix)
    
    submatrix = get_submatrix0n(matrix, n)
    sub_det1 = calculate_determinant(submatrix)

    submatrix = get_submatrixn0(matrix, n)
    sub_det2 = calculate_determinant(submatrix)

    submatrix = get_submatrixnn(matrix, n)
    sub_det3 = calculate_determinant(submatrix)

    submat = get_submatrix00nn(matrix, n-1)
    divisionbyzero = calculate_determinant(submat)
    
    if divisionbyzero == 0:
        divisionbyzeroflag = True
        return 0
    
    return ((sub_det0 * sub_det3) - (sub_det1 * sub_det2)) * (1 / divisionbyzero)

def get_matrix_input():
    global matrix
    global divisionbyzeroflag
    try:
        n = int(size_entry.get())
        matrix = []
        for i in range(n):
            row = list(map(float, matrix_entries[i].get().split()))
            if len(row) != n:
                raise ValueError("Row length does not match matrix size.")
            matrix.append(row)
        determinant = calculate_determinant(matrix)
        if divisionbyzeroflag :
            matrix[0], matrix[1] = matrix[1], matrix[0]
            divisionbyzeroflag = False
            determinant = - calculate_determinant(matrix)
        for i in range(len(matrix)-1):
            if divisionbyzeroflag :
                matrix[i], matrix[i+1] = matrix[i+1], matrix[i]
                divisionbyzeroflag = False
                if i%2 == 0:
                    determinant = - calculate_determinant(matrix)
                determinant = calculate_determinant(matrix)
            else:
                break
        if divisionbyzeroflag:
            messagebox.showerror("Error", "Division by zero encountered.won't work:))))))))")
        else:
            result_label.config(text=f"Determinant: {determinant}")
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Matrix Determinant Calculator")

tk.Label(root, text="Enter the size of the matrix:").grid(row=0, column=0, padx=10, pady=10)
size_entry = tk.Entry(root)
size_entry.grid(row=0, column=1, padx=10, pady=10)

def create_matrix_entries():
    global matrix_entries
    try:
        n = int(size_entry.get())
        for widget in matrix_frame.winfo_children():
            widget.destroy()
        matrix_entries = [tk.Entry(matrix_frame) for _ in range(n)]
        for i, entry in enumerate(matrix_entries):
            tk.Label(matrix_frame, text=f"Row {i+1}:").grid(row=i, column=0, padx=10, pady=5)
            entry.grid(row=i, column=1, padx=10, pady=5)
    except ValueError:
        messagebox.showerror("Input Error", "Invalid size. Please enter a positive integer.")

tk.Button(root, text="Create Matrix Input", command=create_matrix_entries).grid(row=1, column=0, columnspan=2, pady=10)

matrix_frame = tk.Frame(root)
matrix_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

tk.Button(root, text="Calculate Determinant", command=get_matrix_input).grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
