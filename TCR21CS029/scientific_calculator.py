import tkinter as tk
import math
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Scientific Calculator")

        self.display = tk.Entry(master, width=50, borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=8, padx=10, pady=10)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('/', 4, 3),
            ('sin', 1, 4), ('cos', 2, 4), ('tan', 3, 4), ('^', 4, 4),
            ('csc',1,5), ('sec',2,5), ('cot',3,5),('sqr',4,5),
            ('asin',1,6),('acos',2,6),('atan',3,6),('sqr_root',4,6),
            ('lg',1,7),('In',2,7),('X!',3,7),('1/X',4,7)

        ]

        for (text, row, column) in buttons:
            tk.Button(master, text=text, command=lambda t=text: self.click(t)).grid(row=row, column=column, padx= 7)

        self.matrix_entry1 = tk.Entry(master, width=10, borderwidth=3)
        self.matrix_entry1.grid(row=5, column=0, padx=10, pady=10)

        self.matrix_entry2 = tk.Entry(master, width=10, borderwidth=3)
        self.matrix_entry2.grid(row=5, column=1, padx=10, pady=10)

        self.matrix_multiply_button = tk.Button(master, text="Multiply", command=self.matrix_multiply)
        self.matrix_multiply_button.grid(row=5, column=2, padx=10, pady=10)

        self.matrix_add_button = tk.Button(master, text="Add", command=self.matrix_add)
        self.matrix_add_button.grid(row=5, column=3, padx=10, pady=10)

        self.matrix_subtract_button = tk.Button(master, text="Subtract", command=self.matrix_subtract)
        self.matrix_subtract_button.grid(row=5, column=4, padx=10, pady=10)

        tk.Label(self.master, text="Matrix 1").grid(row=6, column=0)
        tk.Label(self.master, text="Matrix 2").grid(row=6, column=1)

        tk.Label(self.master, text="Matrix Operation").grid(row=5, column=5, columnspan=2)

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

        elif button == 'sin':
            try:
                num = float(current)
                result = math.sin(math.radians(num))  # Convert degrees to radians
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")

        elif button == 'cos':
            try:
                num = float(current)
                result = math.cos(math.radians(num))  # Convert degrees to radians
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")

        elif button == 'tan':
            try:
                num = float(current)
                result = math.tan(math.radians(num))  # Convert degrees to radians
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
                
        elif button == '^':
            self.display.insert(tk.END, '**')

        elif button == 'sqr':
            try:
                result = eval(current)**2
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
        
        elif button == 'csc':
            try:
                num = float(current)
                result = 1/math.sin(math.radians(num))  # Convert degrees to radians
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
        
        elif button == 'sec':
            try:
                num = float(current)
                result = 1/math.cos(math.radians(num))  # Convert degrees to radians
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")

        elif button == 'cot':
            try:
                num = float(current)
                result = 1/math.tan(math.radians(num))  # Convert degrees to radians
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")

        elif button == 'asin':
            try:
                num = float(current)
                result = math.asin(num)
                result_degrees = math.degrees(result)   # Convert radian to degree
                formatted_result = "{:.2f}".format(result_degrees)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(formatted_result))
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")

        elif button == 'acos':
            try:
                num = float(current)
                result = math.acos(num)
                result_degrees = math.degrees(result)  # Convert radian to degree
                formatted_result = "{:.2f}".format(result_degrees)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(formatted_result))
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")

        elif button == 'atan':
            try:
                num = float(current)
                result = math.atan(num)
                result_degrees = math.degrees(result)  # Convert radian to degree
                formatted_result = "{:.2f}".format(result_degrees)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(formatted_result))
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")

        elif button == 'sqr_root':
            try:
                result = eval(current)**(1/2)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
        
        elif button == 'lg':
            try:
                result = eval(current)
                log_result = math.log10(result)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(log_result))
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")

        elif button == 'In':
            try:
                result = eval(current)
                log_result = math.log(result)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(log_result))
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")

        elif button == 'X!':
            try:
                result = eval(current)
                fact_result = math.factorial(result)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(fact_result))
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")

        elif button == '1/X':
            try:
                result = 1/eval(current)
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
