import tkinter as tk
from tkinter import messagebox
import numpy as np

#def is_square(matrix):
#    return all(len(row) == len(matrix) for row in matrix)

def determinant(matrix):
    if len(matrix) == 2 and len(matrix[0]) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    det = 0
    for c in range(len(matrix)):
        minor = [row[:c] + row[c+1:] for row in matrix[1:]]
        det += ((-1) ** c) * matrix[0][c] * determinant(minor)
    
    return det

def calculate_determinant(matrix):
#    if not is_square(matrix):
#       raise ValueError("The input must be a square matrix.")
    return determinant(matrix)

class MatrixDeterminantGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Matrix Determinant Calculator")
        
        self.row_label = tk.Label(root, text="Enter number of rows:", font=('Helvetica', 14))
        self.row_label.pack(pady=10)
        #self.n_label = tk.Label(root, text="Enter matrix size (n):", font=('Helvetica', 14))
        #self.n_label.pack(pady=10)
        self.row_entry = tk.Entry(root, font=('Helvetica', 14))
        self.row_entry.pack(pady=10)

        self.col_label = tk.Label(root, text="Enter number of columns:", font=('Helvetica', 14))
        self.col_label.pack(pady=10)
        
        self.col_entry = tk.Entry(root, font=('Helvetica', 14))
        self.col_entry.pack(pady=10)
        
        #self.n_entry = tk.Entry(root, font=('Helvetica', 14))
        #self.n_entry.pack(pady=20)
        
        self.generate_button = tk.Button(root, text="Generate Matrix", font=('Helvetica', 14), command=self.generate_matrix)
        self.generate_button.pack(pady=10)
        
        self.matrix_frame = tk.Frame(root)
        self.matrix_frame.pack(pady=10)
        
        self.calculate_button = tk.Button(root, text="Calculate Determinant", font=('Helvetica', 14), command=self.calculate)
        self.calculate_button.pack(pady=10)
        
        self.result_label = tk.Label(root, text="", font=('Helvetica', 20, 'bold'))
        self.result_label.pack(pady=20)
    
    def generate_matrix(self):
        try:
            rows = int(self.row_entry.get())
            cols = int(self.col_entry.get())
            #n = int(self.n_entry.get())
            if rows <= 0 or cols <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a positive integer for the matrix size.")
            return
        
        for widget in self.matrix_frame.winfo_children():
            widget.destroy()
        
        self.entries = []
        for i in range(rows):
            row_entries = []
            for j in range(cols):
                entry = tk.Entry(self.matrix_frame, width=5, font=('Helvetica', 14))
                entry.grid(row=i, column=j, padx=2, pady=2)
                row_entries.append(entry)
            self.entries.append(row_entries)
    
    def calculate(self):
        try:
            matrix = []
            for row_entries in self.entries:
                row = []
                for entry in row_entries:
                    row.append(float(entry.get()))
                matrix.append(row)
            
            det = calculate_determinant(matrix)
            self.result_label.config(text=f"Determinant: {det}")
        except ValueError as e:
            messagebox.showerror("Invalid input", str(e))
        except Exception as e:
            messagebox.showerror("Error", "Please ensure all matrix entries are valid numbers.")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x350")
    app = MatrixDeterminantGUI(root)
    root.mainloop()
