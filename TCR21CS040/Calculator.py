import tkinter as tk
import math

class ScientificCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Scientific Calculator")
        self.geometry("300x400")
        
        self.entry = tk.Entry(self, width=40)
        self.entry.grid(row=0, column=0, columnspan=5)
        
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("sin", 1, 4), ("cos", 2, 4), ("tan", 3, 4), ("√", 4, 4),
            ("C", 5, 0), ("(", 5, 1), (")", 5, 2), ("ln", 5, 3), ("log", 5, 4),
            ("^", 2, 5), ("DEL", 1, 5)
        ]
        
        for (text, row, col) in buttons:
            button = tk.Button(self, text=text, width=5, height=2, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col)
    
    def on_button_click(self, value):
        if value == "=":
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif value == "C":
            self.entry.delete(0, tk.END)
        elif value == "√":
            try:
                result = math.sqrt(float(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif value in ("sin", "cos", "tan"):
            try:
                func = getattr(math, value)
                result = func(math.radians(float(self.entry.get())))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif value == "ln":
            try:
                result = math.log(float(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif value == "log":
            try:
                result = math.log10(float(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif value == "^":
            self.entry.insert(tk.END, "**")
        elif value == "DEL":
            current_text = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, current_text[:-1])
        else:
            self.entry.insert(tk.END, value)
            
if __name__ == "__main__":
    app = ScientificCalculator()
    app.mainloop()
