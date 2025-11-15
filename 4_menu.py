from tkinter import *
from tkinter import messagebox

root = Tk()

# --- Functions ---
def show_message():
    messagebox.showinfo('First Level', 'A Simple Message')  # First popup message

def show_second_message():
    messagebox.showinfo('Second Level', 'Another Message')  # Second popup message

# --- Menubar ---
menuBar = Menu(root)   # Create main menubar

# Options menu
optionsMenu = Menu(menuBar, tearoff=0)        # Main dropdown menu
menuBar.add_cascade(label='Options', menu=optionsMenu)

optionsMenu.add_command(label='Show Message', command=show_message)  # First menu item
optionsMenu.add_separator()                                           # Divider line

# Submenu
subMenu = Menu(optionsMenu, tearoff=0)      # Create submenu
optionsMenu.add_cascade(label='More Options', menu=subMenu)
subMenu.add_command(label='2nd Level Message', command=show_second_message)  # Submenu item

root.config(menu=menuBar)  # Attach menubar to window

# --- Exit Button ---
Button(root, text='Exit', command=root.quit).pack(pady=20)  # Quit the app

root.mainloop()  # Run the GUI
