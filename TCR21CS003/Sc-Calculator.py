import tkinter as tk
import math



class ScCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Scientific Calculator")
        self.geometry("300x450")
        
        self.entry = tk.Entry(self,bd=10, insertwidth=6, width=35, justify='right', bg="gray", fg="white")
        self.entry.grid(row=0, column=0, columnspan=6, pady=20)
        
        button_params = {'bd': 5, 'fg': '#BBB', 'bg': 'black', 'font': ('Arial', 16, 'bold')}
        button_params_main = {'bd': 5, 'fg': '#000', 'bg': '#BBB', 'font': ('Arial', 16, 'bold')}

        
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("π", 4, 2), ("+", 4, 3),
            ("sin", 1, 4), ("cos", 2, 4), ("tan", 3, 4), ("√", 4, 4),
            ("(", 5, 0), (")", 5, 1), ("%", 5, 2), ("=",5,3),
            ("^", 2, 5), ("EXP", 1, 5),("ln", 3, 5), ("log", 4, 5),("C",5,4),("DEL",5,5)
        ]
        
        for (text, row, col) in buttons:
            button = tk.Button(self, button_params, text=text, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky="nsew")
           
    
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
        elif value in ( "sin","cos", "tan"):
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
        elif value == "EXP":
            self.entry.insert(tk.END, "*10**")
        elif value == "%":
            self.entry.insert(tk.END, "/100")
        elif value == "DEL":
            current_text = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, current_text[:-1])
        elif value == "π":
            self.entry.insert(tk.END, math.pi)
        else:
            self.entry.insert(tk.END, value)
            
if __name__ == "__main__":
    app = ScCalculator()
    app.mainloop()
