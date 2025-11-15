from tkinter import *   # Import tkinter library

root = Tk()             # Create main window

# Create input box for user name
e = Entry(root, width=50, bg='beige', fg='black', borderwidth=5)
e.insert(0, 'Enter Your Name: ')
e.pack()

# Function runs when button is clicked
def myClick():
    message = f'Hello {e.get()}'          # Get name and make greeting
    myLabel = Label(root, text=message)   # Create label with greeting
    myLabel.pack()                        # Show label

# Create and show button that triggers myClick()
myButton = Button(root, text='Confirm', command=myClick, bg='beige', fg='#000000')
myButton.pack()

root.mainloop()         # Keep window open
