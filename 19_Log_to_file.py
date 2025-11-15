from tkinter import *
import logging

# ------------------------------
# Configure logging to write to a file
# ------------------------------
logging.basicConfig(
    filename="./log/app.log",            # Log file name
    level=logging.INFO,            # Log level (INFO and above will be logged)
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def perform_operation(param):
    try:
        # Code that might raise an exception
        result = 10 / param
        logging.info(f"Result: {result}")   # Log successful result
    except ZeroDivisionError as e:
        # Log the error message
        logging.error(f"Error: {e}")

# ------------------------------
# Tkinter GUI
# ------------------------------
root = Tk()
root.title("Logging Demo")

Button(root, text="Normal Operation",
       command=lambda: perform_operation(2)).pack(pady=5)

Button(root, text="Error (Divide by Zero)",
       command=lambda: perform_operation(0)).pack(pady=5)

Button(root, text="Exit Program", command=root.quit).pack(pady=5)

root.mainloop()
