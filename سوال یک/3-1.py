import tkinter as tk
from tkinter import messagebox

def read_matrix(entries, n):
    matrix = []
    try:
        for i in range(n):
            row = [float(entries[i][j].get()) for j in range(n)]
            matrix.append(row)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")
        return None
    return matrix

def determinant(matrix, n):
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        for i in range(n):
            sub_matrix = [row[:i] + row[i + 1:] for row in (matrix[1:])]
            sign = (-1) ** i
            sub_det = determinant(sub_matrix, n - 1)
            det += (sign * matrix[0][i] * sub_det)
        return det

def calculate_determinant():
    try:
        n = int(size_entry.get())
        matrix = read_matrix(entries, n)
        if matrix is not None:
            det = determinant(matrix, n)
            result_label.config(text=f"Determinant: {det}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid matrix size")

def create_matrix_entries():
    global entries
    for widget in matrix_frame.winfo_children():
        widget.destroy()
    try:
        n = int(size_entry.get())
        entries = []
        for i in range(n):
            row_entries = []
            for j in range(n):
                entry = tk.Entry(matrix_frame, width=5)
                entry.grid(row=i, column=j)
                row_entries.append(entry)
            entries.append(row_entries)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid matrix size")

# Set up the main window
root = tk.Tk()
root.title("Matrix Determinant Calculator")

# Matrix size input
size_label = tk.Label(root, text="Matrix size (n x n):")
size_label.pack()

size_entry = tk.Entry(root)
size_entry.pack()

generate_button = tk.Button(root, text="Generate Matrix", command=create_matrix_entries)
generate_button.pack()

# Matrix entries
matrix_frame = tk.Frame(root)
matrix_frame.pack()

# Calculate determinant button
calculate_button = tk.Button(root, text="Calculate Determinant", command=calculate_determinant)
calculate_button.pack()

# Result display
result_label = tk.Label(root, text="Determinant: ")
result_label.pack()

root.mainloop()
