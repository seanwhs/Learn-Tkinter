from tkinter import *
from tkinter import ttk

root = Tk()                                         # Main window
root.title('Simple App to Add User Input to a List')
root.columnconfigure(0, weight=1)                  # Root column expands horizontally
root.rowconfigure(0, weight=1)                     # Root row expands vertically

def addToList(event=None):
    response = entry1.get()                         # Get text from entry
    if response:
        listBox.insert(END, response)               # Add entry text to listbox
        entry1.delete(0, END)                       # Clear entry after adding

frame = ttk.Frame(root)                             # Main frame inside root
frame.grid(row=0, column=0, sticky='nsew')         # Fill entire root
frame.columnconfigure(0, weight=1)                 # Column 0 expands horizontally
frame.columnconfigure(1, weight=1)                 # Column 1 expands horizontally
frame.rowconfigure(1, weight=1)                    # Row 1 (listbox) expands vertically
frame.rowconfigure(2, weight=0)                    # Row 2 (buttons) stays fixed height

entry1 = ttk.Entry(frame)                           # Input field
entry1.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
entry1.bind('<Return>', addToList)                 # Add item on Enter key

btn1 = ttk.Button(frame, text='Add to List', command=addToList)
btn1.grid(row=0, column=1, padx=5, pady=5)        # Button to add entry text

listBox = Listbox(frame)                            # Listbox to display items
listBox.grid(row=1, column=0, columnspan=2, sticky='nsew', padx=5, pady=5)

btn2 = Button(frame, text='Clear List Box', command=lambda: listBox.delete(0, END))
btn2.grid(row=2, column=0, sticky='ew', padx=5, pady=5)  # Clear button

btn3 = Button(frame, text='Exit Program', command=root.quit)
btn3.grid(row=2, column=1, sticky='ew', padx=5, pady=5)  # Exit button

root.mainloop()                                     # Start the GUI event loop
