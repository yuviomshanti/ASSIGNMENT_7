import tkinter as tk

def button_click(number):
    current_expression = expression_label['text']
    new_expression = current_expression + str(number)
    expression_label['text'] = new_expression

def clear():
    expression_label['text'] = ""

def calculate():
    expression = expression_label['text']
    try:
        result = eval(expression)
        expression_label['text'] = str(result)
    except Exception:
        expression_label['text'] = "Error"

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create the expression label
expression_label = tk.Label(window, text="", width=20)
expression_label.grid(row=0, column=0, columnspan=4)

# Create number buttons
button_1 = tk.Button(window, text="1", command=lambda: button_click(1))
button_2 = tk.Button(window, text="2", command=lambda: button_click(2))
button_3 = tk.Button(window, text="3", command=lambda: button_click(3))
button_4 = tk.Button(window, text="4", command=lambda: button_click(4))
button_5 = tk.Button(window, text="5", command=lambda: button_click(5))
button_6 = tk.Button(window, text="6", command=lambda: button_click(6))
button_7 = tk.Button(window, text="7", command=lambda: button_click(7))
button_8 = tk.Button(window, text="8", command=lambda: button_click(8))
button_9 = tk.Button(window, text="9", command=lambda: button_click(9))
button_0 = tk.Button(window, text="0", command=lambda: button_click(0))

# Create operation buttons
button_add = tk.Button(window, text="+", command=lambda: button_click("+"))
button_subtract = tk.Button(window, text="-", command=lambda: button_click("-"))
button_multiply = tk.Button(window, text="*", command=lambda: button_click("*"))
button_divide = tk.Button(window, text="/", command=lambda: button_click("/"))
button_equal = tk.Button(window, text="=", command=calculate)
button_clear = tk.Button(window, text="C", command=clear)

# Place the buttons on the grid
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_add.grid(row=1, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_subtract.grid(row=2, column=3)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_multiply.grid(row=3, column=3)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1)
button_equal.grid(row=4, column=2)
button_divide.grid(row=4, column=3)

# Start the main loop
window.mainloop()

