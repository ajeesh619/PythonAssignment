import tkinter as tk
import math


def update_entry(result):
    entry.delete(0, tk.END)
    entry.insert(tk.END, result)


def calculate():
    try:
        result = eval(entry.get())
        update_entry(result)
    except Exception as e:
        update_entry("Error")

def clear():
    entry.delete(0, tk.END)

def trig_function(func_name, func):
    def wrapper():
        try:
            result = func(math.radians(float(entry.get())))
            update_entry(f"{func_name}({entry.get()}) = {result}")
        except Exception as e:
            update_entry("Error")
    return wrapper

def log_function(func_name, func):
    def wrapper():
        try:
            result = func(float(entry.get()))
            update_entry(f"{func_name}({entry.get()}) = {result}")
        except Exception as e:
            update_entry("Error")
    return wrapper

def exp_function():
    try:
        result = math.exp(float(entry.get()))
        update_entry(f"exp({entry.get()}) = {result}")
    except Exception as e:
        update_entry("Error")

def power_function():
    try:
        power = float(input("Enter the power: "))
        result = math.pow(float(entry.get()), power)
        update_entry(f"({entry.get()})^{power} = {result}")
    except Exception as e:
        update_entry("Error")

def root_function():
    try:
        n = float(input("Enter the root: "))
        result = math.pow(float(entry.get()), 1/n)
        update_entry(f"ⁿ√{entry.get()} = {result}")
    except Exception as e:
        update_entry("Error")

def factorial():
    try:
        result = math.factorial(int(entry.get()))
        update_entry(f"{entry.get()}! = {result}")
    except Exception as e:
        update_entry("Error")

def percentage():
    try:
        result = float(entry.get()) / 100
        update_entry(f"{entry.get()}% = {result}")
    except Exception as e:
        update_entry("Error")

def angle_conversion(func_name, func):
    def wrapper():
        try:
            result = func(float(entry.get()))
            update_entry(f"{func_name}({entry.get()}) = {result}")
        except Exception as e:
            update_entry("Error")
    return wrapper

def insert_constant(constant):
    entry.insert(tk.END, constant)


root = tk.Tk()
root.title("Scientific Calculator")


entry = tk.Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=6)


trig_funcs = [("sin", trig_function("sin", math.sin)), 
              ("cos", trig_function("cos", math.cos)), 
              ("tan", trig_function("tan", math.tan)), 
              ("asin", trig_function("asin", math.asin)), 
              ("acos", trig_function("acos", math.acos)), 
              ("atan", trig_function("atan", math.atan))]

for i, (name, func) in enumerate(trig_funcs):
    btn = tk.Button(root, text=name, padx=20, pady=10, command=func)
    btn.grid(row=1, column=i)


log_funcs = [("ln", log_function("ln", math.log)), 
             ("log", log_function("log", math.log10)), 
             ("log𝑏", log_function("log𝑏", lambda x: math.log(x, 2)))]

for i, (name, func) in enumerate(log_funcs):
    btn = tk.Button(root, text=name, padx=20, pady=10, command=func)
    btn.grid(row=2, column=i)


btn_exp = tk.Button(root, text="exp", padx=20, pady=10, command=exp_function)
btn_exp.grid(row=3, column=0)


btn_power = tk.Button(root, text="x^y", padx=20, pady=10, command=power_function)
btn_power.grid(row=3, column=1)

btn_root = tk.Button(root, text="ⁿ√x", padx=20, pady=10, command=root_function)
btn_root.grid(row=3, column=2)


btn_factorial = tk.Button(root, text="n!", padx=20, pady=10, command=factorial)
btn_factorial.grid(row=4, column=0)


btn_percentage = tk.Button(root, text="%", padx=20, pady=10, command=percentage)
btn_percentage.grid(row=4, column=1)


angle_funcs = [("Deg to Rad", angle_conversion("deg_to_rad", math.radians)), 
               ("Rad to Deg", angle_conversion("rad_to_deg", math.degrees))]

for i, (name, func) in enumerate(angle_funcs):
    btn = tk.Button(root, text=name, padx=20, pady=10, command=func)
    btn.grid(row=4, column=i+2)


btn_pi = tk.Button(root, text="π", padx=20, pady=10, command=lambda: insert_constant(math.pi))
btn_pi.grid(row=5, column=0)

btn_e = tk.Button(root, text="𝑒", padx=20, pady=10, command=lambda: insert_constant(math.e))
btn_e.grid(row=5, column=1)


button_numbers = [
    ("7", 6, 0), ("8", 6, 1), ("9", 6, 2),
    ("4", 7, 0), ("5", 7, 1), ("6", 7, 2),
    ("1", 8, 0), ("2", 8, 1), ("3", 8, 2),
    ("0", 9, 1), (".", 9, 2)
]

for (text, row, column) in button_numbers:
    button = tk.Button(root, text=text, padx=20, pady=10, command=lambda t=text: entry.insert(tk.END, t))
    button.grid(row=row, column=column)


btn_equal = tk.Button(root, text="=", padx=20, pady=10, command=calculate)
btn_equal.grid(row=9, column=3, columnspan=2)

btn_clear = tk.Button(root, text="C", padx=20, pady=10, command=clear)
btn_clear.grid(row=6, column=3, columnspan=2)

root.mainloop()
