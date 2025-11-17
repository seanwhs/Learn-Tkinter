from tkinter import *
import logging
import os

# ------------------------------
# Ensure log directory exists
# ------------------------------
log_dir = "./log"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# ------------------------------
# Configure two loggers: console and file
# ------------------------------

# Logger for console output
console_logger = logging.getLogger("console_logger")
console_logger.setLevel(logging.INFO)                       # Log INFO and above
console_handler = logging.StreamHandler()                   # Output to console
console_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console_handler.setFormatter(console_formatter)
console_logger.addHandler(console_handler)

# Logger for file output
file_logger = logging.getLogger("file_logger")
file_logger.setLevel(logging.INFO)                          # Log INFO and above
file_handler = logging.FileHandler(f"{log_dir}/app.log")    # Output to file
file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
file_logger.addHandler(file_handler)

# ------------------------------
# Function to perform an operation
# ------------------------------
def perform_operation(param):
    try:
        result = 10 / param                                 # May raise ZeroDivisionError
        console_logger.info(f"Console log: Result = {result}")
        file_logger.info(f"File log: Result = {result}")
    except ZeroDivisionError as e:
        console_logger.error(f"Console log: Error = {e}")
        file_logger.error(f"File log: Error = {e}")

# ------------------------------
# Tkinter GUI
# ------------------------------
root = Tk()
root.title("Logging Comparison")
root.geometry("350x180")

# Buttons to trigger operations
Button(root, text="Normal Operation", width=30,
       command=lambda: perform_operation(2)).pack(pady=10)

Button(root, text="Error (Divide by Zero)", width=30,
       command=lambda: perform_operation(0)).pack(pady=10)

Button(root, text="Exit Program", width=30, command=root.quit).pack(pady=10)

root.mainloop()
