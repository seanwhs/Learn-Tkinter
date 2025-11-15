from tkinter import *
import logging

def perform_operation(param):
    try:
        # Code that might raise an exception
        result = 10 / param
        logging.info(f"Result: {result}")
    except ZeroDivisionError as e:
        # Log the error
        logging.error(f"Error: {e}")

root = Tk()

Button(root, text="Normal Operation", command=lambda:perform_operation(2)).pack(pady=5)
Button(root, text="Error", command=lambda:perform_operation(0)).pack(pady=5)
Button(root, text="Exit Program", command=root.quit).pack(pady=5)

root.mainloop()