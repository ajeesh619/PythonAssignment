import tkinter as tk
import math

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        
        self.result_var = tk.StringVar()
        
        self.create_widgets()
        
    def create_widgets(self):
        # Entry widget to display result
        self.result_entry = tk.Entry(self.root, textvariable=self.result_var, font=('Helvetica', 14), bd=10, insertwidth=4, width=25, justify='right')
        self.result_entry.grid(row=0, column=0, columnspan=5)
        
        # Buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('sin', 1, 4), ('cos', 2, 4), ('tan', 3, 4), ('sqrt', 4, 4)
        ]
        
        for (text, row, column) in buttons:
            button = tk.Button(self.root, text=text, font=('Helvetica', 14), bd=5, padx=15, pady=10, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=column)
        
    def on_button_click(self, char):
        if char == '=':
            try:
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        elif char == 'sqrt':
            try:
                result = math.sqrt(float(self.result_var.get()))
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        elif char == 'sin':
            try:
                result = math.sin(math.radians(float(self.result_var.get())))
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        elif char == 'cos':
            try:
                result = math.cos(math.radians(float(self.result_var.get())))
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        elif char == 'tan':
            try:
                result = math.tan(math.radians(float(self.result_var.get())))
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        else:
            current_text = self.result_var.get()
            self.result_var.set(current_text + char)

def main():
    root = tk.Tk()
    calculator = ScientificCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
