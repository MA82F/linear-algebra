import tkinter as tk
from tkinter import messagebox
import numpy as np

def calculate_determinant(matrix):
    try:
        n = len(matrix)
        A = np.array(matrix, dtype=float)
        det = 1
        for i in range(n):
            pivot = A[i, i]
            if pivot == 0:
                for j in range(i + 1, n):
                    if A[j, i] != 0:
                        A[[i, j]] = A[[j, i]]
                        pivot = A[i, i]
                        det *= -1  # Swap rows changes the sign of determinant
                        break
            if pivot == 0:
                return 0
            det *= pivot
            A[i] = A[i] / pivot
            for j in range(n):
                if j != i:
                    factor = A[j, i]
                    A[j] = A[j] - factor * A[i]
        return round(det, 10)  # Round the determinant to avoid floating point precision issues
    except Exception as e:
        messagebox.showerror("Error", str(e))
        return None

def get_matrix_input():
    try:
        matrix = []
        for row in matrix_entries:
            matrix.append([float(entry.get()) for entry in row])
        return matrix
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers in the matrix.")
        return None

def on_calculate():
    matrix = get_matrix_input()
    if matrix is not None:
        determinant = calculate_determinant(matrix)
        if determinant is not None:
            result_label.config(text=f"Determinant: {determinant}")

def on_size_change():
    global matrix_entries
    try:
        rows = int(rows_entry.get())
        cols = int(cols_entry.get())
        if rows < 1 or cols < 1 or rows != cols:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid matrix dimensions (positive integers and square matrix).")
        return

    for widget in matrix_frame.winfo_children():
        widget.destroy()

    matrix_entries = []
    for i in range(rows):
        row_entries = []
        for j in range(cols):
            entry = tk.Entry(matrix_frame, width=5)
            entry.grid(row=i, column=j)
            row_entries.append(entry)
        matrix_entries.append(row_entries)

root = tk.Tk()
root.title("Matrix Determinant Calculator")

instructions = tk.Label(root, text="Enter the dimensions of the matrix:")
instructions.grid(row=0, column=0, columnspan=4)

rows_label = tk.Label(root, text="Rows:")
rows_label.grid(row=1, column=0)
rows_entry = tk.Entry(root, width=5)
rows_entry.grid(row=1, column=1)
rows_entry.insert(0, "3")

cols_label = tk.Label(root, text="Cols:")
cols_label.grid(row=1, column=2)
cols_entry = tk.Entry(root, width=5)
cols_entry.grid(row=1, column=3)
cols_entry.insert(0, "3")

size_button = tk.Button(root, text="Set Size", command=on_size_change)
size_button.grid(row=2, column=0, columnspan=4)

matrix_frame = tk.Frame(root)
matrix_frame.grid(row=3, column=0, columnspan=4)

matrix_entries = []
on_size_change()

calculate_button = tk.Button(root, text="Calculate Determinant", command=on_calculate)
calculate_button.grid(row=4, column=0, columnspan=4)

result_label = tk.Label(root, text="Determinant: ")
result_label.grid(row=5, column=0, columnspan=4)

root.mainloop()
