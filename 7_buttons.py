from tkinter import *   # Import all classes and functions from the tkinter library

root = Tk()             # Create the main application window

def myClick():
    # Create a label widget with text and add it to the window
    myLabel = Label(root, text='Look! I Clicked a Button!!!')
    myLabel.pack()

# Create a button widget with custom colors and assign a click function
myButton = Button(root, text='Click me!', command=myClick, bg='red', fg='#000000')
myButton.pack()

root.mainloop()         # Run the main event loop to keep the window open
