from tkinter import *

root = Tk()

def buttonProperties():
    print(btn.config().keys())

def labelProperties():
    print(lbl.config().keys())

def entryProperties():
    print(entry.config().keys())

# Define widegets but don'e display them 
btn = Button(root)
lbl = Label(root)
entry = Entry(root)

# Buttons to show widget properties
Button(root, text='Button Props', command=buttonProperties).grid(row=1, column=0)
Button(root, text='Label Props', command=labelProperties).grid(row=1, column=1)
Button(root, text='Entry Props', command=entryProperties).grid(row=1, column=2)

# Exit button
Button(root, text='Exit Program', command=root.quit).grid(row=2, column=2)

root.mainloop()
