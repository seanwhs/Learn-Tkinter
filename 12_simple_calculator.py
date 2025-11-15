from tkinter import *   # Import tkinter library

root = Tk()             # Create main window
root.title('Simple Calculator')

# Create input box for numbers
e = Entry(root, width=35, borderwidth=5, bg='beige', fg='#000000')
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# ----- Functions -----
def button_click(number):
    """Append clicked number to entry"""
    current = e.get()
    button_clear_all()
    e.insert(0, str(current) + str(number))

def button_clear_all():
    """Clear entry field"""
    e.delete(0, END)

def button_plus():
    """Prepare addition operation"""
    global operation
    operation = 'addition'
    save_first_number()
    button_clear_all()

def button_minus():
    """Prepare subtraction operation"""
    save_first_number()
    button_clear_all()
    save_operation('subtraction')

def button_times():
    """Prepare multiplication operation"""
    save_first_number()
    button_clear_all()
    save_operation('multiplication')

def button_into():
    """Prepare division operation"""
    save_first_number()
    button_clear_all()
    save_operation('division')

def button_result():
    """Calculate and display result"""
    save_second_number()
    button_clear_all()
    if operation == 'addition': 
        e.insert(0, first_number + second_number)
    elif operation == 'subtraction': 
        e.insert(0, first_number - second_number)
    elif operation == 'multiplication': 
        e.insert(0, first_number * second_number)
    elif operation == 'division': 
        e.insert(0, first_number / second_number)
    else:
        e.insert(0, 'error') 

def save_first_number():
    """Store first number for operation"""
    global first_number
    first_number = float(e.get())

def save_second_number():
    """Store second number for operation"""
    global second_number
    second_number = float(e.get())

def save_operation(operator):
    """Store operation type"""
    global operation
    operation = operator

# ----- Number Buttons -----
button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_click(0))

# ----- Operation Buttons -----
button_add = Button(root, text='+', padx=39, pady=20, command=button_plus)
button_subtract = Button(root, text='-', padx=40, pady=20, command=button_minus)
button_multiply = Button(root, text='*', padx=40, pady=20, command=button_times)
button_divide = Button(root, text='/', padx=40, pady=20, command=button_into)

# ----- Utility Buttons -----
button_equal = Button(root, text='=', padx=85, pady=20, command=button_result)
button_clear = Button(root, text='Clear', padx=76, pady=20, command=button_clear_all)

# ----- Place Buttons on Screen -----
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)

button_clear.grid(row=4, column=1, columnspan=2)
button_equal.grid(row=5, column=1, columnspan=2)

button_add.grid(row=5, column=0)
button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

root.mainloop()  # Run the application
