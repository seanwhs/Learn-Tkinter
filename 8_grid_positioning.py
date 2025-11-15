from tkinter import *   # Import tkinter library

root = Tk()             # Create main window

# Create text labels
myLabel1 = Label(root, text='Hello World')
myLabel2 = Label(root, text='My Name is Sean Wong')
myLabel3 = Label(root, text='                    ')  # Empty space label
myLabel4 = Label(root, text='And I love tkinter!')

# Place labels on a grid (row, column positions)
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)
myLabel3.grid(row=1, column=2)
myLabel4.grid(row=5, column=3)

root.mainloop()         # Keep window open and responsive
