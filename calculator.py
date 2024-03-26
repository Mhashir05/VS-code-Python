import tkinter as tk
import math

def button_click(char):
    current = display_var.get()
    if char == "C":
        display_var.set("")
    elif char == "=":
        try:
            result = eval(current)
            display_var.set(str(result))
        except:
            display_var.set("Error")
    elif char == "sqrt":
        try:
            result = math.sqrt(float(current))
            display_var.set(str(result))
        except:
            display_var.set("Error")
    elif char == "^2":
        try:
            result = float(current) ** 2
            display_var.set(str(result))
        except:
            display_var.set("Error")
    elif char == "^3":
        try:
            result = float(current) ** 3
            display_var.set(str(result))
        except:
            display_var.set("Error")
    elif char == "%":
        try:
            result = float(current) / 100
            display_var.set(str(result))
        except:
            display_var.set("Error")
    else:
        display_var.set(current + char)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create a variable to store the current display text
display_var = tk.StringVar()
display_var.set("")

# Create the display label
display_label = tk.Label(root, textvariable=display_var, font=("Arial", 20), anchor="e", padx=10)
display_label.grid(row=0, column=0, columnspan=4)

# Define buttons
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "C", "sqrt", "^2", "^3",
    "%"
]

# Create and position buttons
for i, char in enumerate(buttons):
    row = i // 4 + 1
    col = i % 4
    button = tk.Button(root, text=char, font=("Arial", 16), width=5, height=2, command=lambda c=char: button_click(c))
    button.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
