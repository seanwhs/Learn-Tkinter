from tkinter import *

# Create the main application window
root = Tk()
root.title("Entry Validation Example")

# Validation function (returns True if valid, False otherwise)
def only_numbers(new_value):
    """
    This function is called every time the user types something.
    new_value = the value of the Entry *after* the key press.

    Return True → accept the change.
    Return False → reject the change.
    """
    # Allow empty string (so user can delete text)
    if new_value == "":
        return True
    
    # Allow digits only (no letters, spaces, symbols, etc.)
    return new_value.isdigit()

# Register the validation function with Tkinter
# Tkinter requires this to be able to call Python functions for validation
validate_cmd = root.register(only_numbers)

# Label for instruction
Label(root, text="Enter numbers only:").pack(pady=5)

# Entry widget with validation enabled
entry = Entry(
    root,
    validate="key",                 # Validate on every keystroke
    validatecommand=(validate_cmd, "%P")  # %P = proposed new value
)
entry.pack(pady=5, padx=10)

# Button to exit the application
Button(root, text='Exit Program', command=root.quit).pack(padx=5, pady=5)

# Start the Tkinter event loop
root.mainloop()
