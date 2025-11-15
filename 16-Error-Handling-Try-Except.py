from tkinter import *
from tkinter import messagebox

# Create main application window
root = Tk()
root.title('Try-Except Block Demo')

def divide(denominator):
    """
    Attempts to divide 10 by the given denominator.
    Shows a message box with result if successful,
    otherwise catches ZeroDivisionError and shows an error message.
    """
    try:
        # Try performing the division
        result = 10 / denominator
        
        # Show result in an info message box
        messagebox.showinfo('Result', f'Result: {result}')
    
    except ZeroDivisionError:
        # Handle division-by-zero errors
        messagebox.showerror('Error', 'Cannot divide by Zero!')

# Button that triggers a division-by-zero error
Button(root, text='Divide By Zero Error', command=lambda: divide(0)).pack(padx=5, pady=5)

# Button that performs a normal division (10/2)
Button(root, text='Normal Division', command=lambda: divide(2)).pack(padx=5, pady=5)

# Button to exit the application
Button(root, text='Exit Program', command=root.quit).pack(padx=5, pady=5)

# Start the Tkinter event loop
root.mainloop()
