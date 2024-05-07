from tkinter import *
import math

def append_character(char):
    global expression
    expression += str(char)
    text_input.set(expression)

def clear_all():
    global expression
    expression = ""
    text_input.set("")

def delete_last():
    global expression
    text = expression[:-1]
    expression = text
    text_input.set(text)

def calculate_factorial():
    global expression
    result = str(factorial(int(expression)))
    expression = result
    text_input.set(result)

def calculate_sin():
    global expression
    result = str(math.sin(math.radians(int(expression))))
    expression = result
    text_input.set(result)

def calculate_cos():
    global expression
    result = str(math.cos(math.radians(int(expression))))
    expression = result
    text_input.set(result)

def calculate_tan():
    global expression
    result = str(math.tan(math.radians(int(expression))))
    expression = result
    text_input.set(result)

def calculate_cot():
    global expression
    result = str(1/math.tan(math.radians(int(expression))))
    expression = result
    text_input.set(result)

def calculate_square_root():
    global expression
    if int(expression) >= 0:
        temp = str(eval(expression+'**(1/2)'))
        expression = temp
    else:
        temp = "ERROR"
    text_input.set(temp)

def calculate_cube_root():
    global expression
    if int(expression) >= 0:
        temp = str(eval(expression+'**(1/3)'))
        expression = temp
    else:
        temp = "ERROR"
    text_input.set(temp)

def change_sign():
    global expression
    if expression[0] == '-':
        temp = expression[1:]
    else:
        temp = '-'+expression
    expression = temp
    text_input.set(temp)

def calculate_percentage():
    global expression
    temp = str(eval(expression+'/100'))
    expression = temp
    text_input.set(temp)

def calculate_result():
    global expression
    temp_op = str(eval(expression))
    text_input.set(temp_op)
    expression = temp_op

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)

tk_calc = Tk()
tk_calc.configure(bg="#293C4A", bd=10)
tk_calc.title("Scientific Calculator")

expression = ""
text_input = StringVar()

text_display = Entry(tk_calc, font=('sans-serif', 20, 'bold'), textvariable=text_input,
                     bd=5, insertwidth=5, bg='#BBB', justify='right').grid(columnspan=5, padx=10, pady=15)

button_params = {'bd':5, 'fg':'#BBB', 'bg':'#3C3636', 'font':('sans-serif', 20, 'bold')}
button_params_main = {'bd':5, 'fg':'#000', 'bg':'#BBB', 'font':('sans-serif', 20, 'bold')}

buttons = [
    ('C', clear_all), ('DEL', delete_last), ('x!', calculate_factorial), ('%', calculate_percentage), ('AC', clear_all),
    ('sin', calculate_sin), ('cos', calculate_cos), ('tan', calculate_tan), ('cot', calculate_cot), ('π', lambda: append_character(math.pi)),
    ('x²', lambda: append_character('**2')), ('x³', lambda: append_character('**3')), ('xⁿ', lambda: append_character('**')), ('¹/x', lambda: append_character('**(-1)')), ('10^x', lambda: append_character('10**')),
    ('√', calculate_square_root), ('³√', calculate_cube_root), ('√', lambda: append_character('**(1/')), ('log₁₀', lambda: append_character('log(')), ('ln', lambda: append_character('ln(')),
    ('(', lambda: append_character('(')), (')', lambda: append_character(')')), ('±', change_sign), ('.', lambda: append_character('.')), ('EXP', lambda: append_character('*10**')),
    ('7', lambda: append_character('7')), ('8', lambda: append_character('8')), ('9', lambda: append_character('9')), ('/', lambda: append_character('/')), ('mod', lambda: append_character('%')),
    ('4', lambda: append_character('4')), ('5', lambda: append_character('5')), ('6', lambda: append_character('6')), ('*', lambda: append_character('*')), ('div', lambda: append_character('//')),
    ('1', lambda: append_character('1')), ('2', lambda: append_character('2')), ('3', lambda: append_character('3')), ('-', lambda: append_character('-')),
    ('0', lambda: append_character('0')), ('±', change_sign), ('.', lambda: append_character('.')), ('+', lambda: append_character('+')), ('=', calculate_result)
]

row = 1
col = 0
for (text, command) in buttons:
    Button(tk_calc, button_params_main, text=text, command=command).grid(row=row, column=col, sticky="nsew")
    col += 1
    if col > 4:
        col = 0
        row += 1

tk_calc.mainloop()
