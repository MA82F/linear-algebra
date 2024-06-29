import tkinter as tk
from tkinter import messagebox
import numpy as np

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

def get_matrix_input():
    try:
        matrix = []
        for row in matrix_entries:
            matrix.append([int(entry.get()) for entry in row])
        return matrix
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid integers in the matrix.")
        return None

def on_calculate():
    matrix = get_matrix_input()
    if matrix is not None:
        determinant = calculate_determinant(matrix)
        result_label.config(text=f"Determinant: {determinant}")

def on_size_change():
    global matrix_entries
    try:
        size = int(size_entry.get())
        if size < 1:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid matrix size (positive integer).")
        return

    for widget in matrix_frame.winfo_children():
        widget.destroy()

    matrix_entries = []
    for i in range(size):
        row_entries = []
        for j in range(size):
            entry = tk.Entry(matrix_frame, width=5)
            entry.grid(row=i, column=j)
            row_entries.append(entry)
        matrix_entries.append(row_entries)

root = tk.Tk()
root.title("Matrix Determinant Calculator")

instructions = tk.Label(root, text="Enter the size of the matrix:")
instructions.grid(row=0, column=0, columnspan=2)

size_entry = tk.Entry(root, width=5)
size_entry.grid(row=0, column=2)
size_entry.insert(0, "3")

size_button = tk.Button(root, text="Set Size", command=on_size_change)
size_button.grid(row=0, column=3)

matrix_frame = tk.Frame(root)
matrix_frame.grid(row=1, column=0, columnspan=4)

matrix_entries = []
on_size_change()

calculate_button = tk.Button(root, text="Calculate Determinant", command=on_calculate)
calculate_button.grid(row=2, column=0, columnspan=4)

result_label = tk.Label(root, text="Determinant: ")
result_label.grid(row=3, column=0, columnspan=4)

root.mainloop()
