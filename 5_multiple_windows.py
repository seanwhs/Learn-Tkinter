from tkinter import *

# Function to open a new window
def open_new_window():
    newWindow = Toplevel(root)        # Create a new top-level window
    newWindow.title('New Window')     # Set window title

    Label(newWindow, text='This is a new Window.').pack(pady=10)  # Add label
    Button(newWindow, text='Close Window', 
           command=newWindow.destroy).pack(pady=10)  # Close only this window

root = Tk()
root.title('Main Window')             # Main window title

Label(root).pack(padx=10, pady=10)    # Empty spacer label

Button(root, text='Open New Window', 
       command=open_new_window).pack(pady=20)  # Button to open new window

Button(root, text='Close Application', 
       command=root.quit).pack(pady=20)  # Exit whole application

root.mainloop()                         # Run the GUI loop
