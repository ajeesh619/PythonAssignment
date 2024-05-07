import tkinter as tk
import math
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Scientific Calculator")

        # Color Scheme
        bg_color = "#000000"  # black
        btn_color = "#4CAF50"  # Green
        btn_hover_color = "#45a049"  # Darker green
        text_color = "#333333"  # Dark gray

        # Styling
        master.geometry("400x700")
        master.configure(bg=bg_color)

        # Display
        self.display = tk.Entry(master, width=30, font=('Arial', 14), borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        # Button Grid
        buttons = [
            ('sin', 1, 0), ('cos', 1, 1), ('tan', 1, 2), ('^', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('0', 5, 0), ('.', 5, 1), ('C', 5, 2), ('=', 5, 3)
        ]

        additional_buttons = [
            ('asin', 6, 0), ('sqr', 6, 1), ('sqr_root', 6, 2), ('lg', 6, 3),
            ('In', 7, 0), ('X!', 7, 1), ('1/X', 7, 2), ('cot', 7, 3)
        ]

        buttons.extend(additional_buttons)

        for (text, row, column) in buttons:
            btn = tk.Button(master, text=text, command=lambda t=text: self.click(t), padx=15, pady=15, font=('Arial', 12),
                            bg=btn_color, fg="white", activebackground=btn_hover_color, activeforeground="white")
            btn.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")

        # Matrix Entry
        tk.Label(master, text="Matrix 1").grid(row=8, column=0, padx=5, pady=5)
        tk.Label(master, text="Matrix 2").grid(row=8, column=1, padx=5, pady=5)

        self.matrix_entry1 = tk.Entry(master, width=10, borderwidth=3)
        self.matrix_entry1.grid(row=9, column=0, padx=5, pady=5)

        self.matrix_entry2 = tk.Entry(master, width=10, borderwidth=3)
        self.matrix_entry2.grid(row=9, column=1, padx=5, pady=5)

        # Matrix Operation Buttons
        matrix_operations = [
            ('Multiply', self.matrix_multiply, 0, btn_color),
            ('Add', self.matrix_add, 1, btn_color),
            ('Subtract', self.matrix_subtract, 2, btn_color)
        ]

        for (text, command, column, color) in matrix_operations:
            btn = tk.Button(master, text=text, command=command, padx=10, pady=10, font=('Arial', 10),
                            bg=color, fg="white", activebackground=btn_hover_color, activeforeground="white")
            btn.grid(row=9, column=column+2, padx=5, pady=5, sticky="nsew")

        # History Display
        self.history_display = tk.Text(master, height=5, width=30, font=('Arial', 12), borderwidth=2)
        self.history_display.grid(row=10, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        # Configure Grid
        for i in range(11):
            master.grid_rowconfigure(i, weight=1)
        for i in range(4):
            master.grid_columnconfigure(i, weight=1)

    def click(self, button):
        current = self.display.get()

        if button == '=':
            try:
                result = eval(current)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")

        elif button == 'C':
            self.display.delete(0, tk.END)

        elif button in ['sin', 'cos', 'tan', '^', 'sqr', 'csc', 'sec', 'cot', 'asin', 'acos', 'atan', 'sqr_root', 'lg', 'In', 'X!', '1/X']:
            # Handle trigonometric and other functions
            try:
                num = float(current)
                if button == '^':
                    self.display.insert(tk.END, '**')
                elif button == 'sqr':
                    result = eval(current)**2
                    self.display.delete(0, tk.END)
                    self.display.insert(tk.END, str(result))
                elif button == 'sqr_root':
                    result = eval(current)**(1/2)
                    self.display.delete(0, tk.END)
                    self.display.insert(tk.END, str(result))
                elif button == 'lg':
                    result = math.log10(eval(current))
                    self.display.delete(0, tk.END)
                    self.display.insert(tk.END, str(result))
                elif button == 'In':
                    result = math.log(eval(current))
                    self.display.delete(0, tk.END)
                    self.display.insert(tk.END, str(result))
                elif button == 'X!':
                    result = math.factorial(eval(current))
                    self.display.delete(0, tk.END)
                    self.display.insert(tk.END, str(result))
                elif button == '1/X':
                    result = 1/eval(current)
                    self.display.delete(0, tk.END)
                    self.display.insert(tk.END, str(result))
                else:
                    # Handle trigonometric functions
                    result = getattr(math, button)(math.radians(num))  # Convert degrees to radians
                    self.display.delete(0, tk.END)
                    self.display.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")

        else:
            self.display.insert(tk.END, button)

    def matrix_multiply(self):
        matrix1_str = self.matrix_entry1.get()
        matrix2_str = self.matrix_entry2.get()

        try:
            matrix1 = eval(matrix1_str)
            matrix2 = eval(matrix2_str)

            result = self.perform_matrix_multiply(matrix1, matrix2)
            messagebox.showinfo("Result", "Result of matrix multiplication:\n" + str(result))
        except Exception as e:
            messagebox.showerror("Error", "Matrix multiplication failed: " + str(e))

    def matrix_add(self):
        matrix1_str = self.matrix_entry1.get()
        matrix2_str = self.matrix_entry2.get()

        try:
            matrix1 = eval(matrix1_str)
            matrix2 = eval(matrix2_str)

            result = self.perform_matrix_addition(matrix1, matrix2)
            messagebox.showinfo("Result", "Result of matrix addition:\n" + str(result))
        except Exception as e:
            messagebox.showerror("Error", "Matrix addition failed: " + str(e))

    def matrix_subtract(self):
        matrix1_str = self.matrix_entry1.get()
        matrix2_str = self.matrix_entry2.get()

        try:
            matrix1 = eval(matrix1_str)
            matrix2 = eval(matrix2_str)

            result = self.perform_matrix_subtraction(matrix1, matrix2)
            messagebox.showinfo("Result", "Result of matrix subtraction:\n" + str(result))
        except Exception as e:
            messagebox.showerror("Error", "Matrix subtraction failed: " + str(e))

    def perform_matrix_multiply(self, matrix1, matrix2):
        result = [[sum(a*b for a,b in zip(matrix1_row, matrix2_col)) for matrix2_col in zip(*matrix2)] for matrix1_row in matrix1]
        return result

    def perform_matrix_addition(self, matrix1, matrix2):
        result = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
        return result

    def perform_matrix_subtraction(self, matrix1, matrix2):
        result = [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
        return result

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()