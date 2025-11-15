from tkinter import *

root = Tk()

# Main title
Label(root, text="Tkinter Widgets").pack()

# Status label (shows user actions)
statusLabel = Label(root, text="Make a selection", padx=200)
statusLabel.pack()

# --- Helper Functions ---

def update_check_status(var, widget_type):
    """Update status when a checkbutton or radiobutton is used."""
    value = var.get()

    if widget_type == 'check':
        msg = "Check Button"
        status = "selected" if value else "NOT selected"
    else:  # radio button
        msg = "Radio Button"
        status = f"selected: {value}"

    statusLabel.config(text=f"{msg} is {status}")

def listBoxEvent(event):
    """Update status when a listbox item is selected."""
    if myListBox.curselection():
        item = myListBox.get(myListBox.curselection())
        statusLabel.config(text=f"listBox selected: {item}")

def entryEvent(*args):
    """Update status with what the user types."""
    statusLabel.config(text=f"You entered {myEntry.get()}.")

def button_toggle():
    """Toggle ON/OFF button text."""
    toggle['text'] = 'OFF' if toggle['text'] == 'ON' else 'ON'

# --- Widgets ---

# Checkbutton
myCheckVar = BooleanVar()
Checkbutton(
    root,
    text="Check Me",
    variable=myCheckVar,
    command=lambda: update_check_status(myCheckVar, 'check')
).pack()

# Radiobuttons
myRadioVar = StringVar(value='Option 1')

Radiobutton(
    root,
    text="Option 1",
    variable=myRadioVar,
    value="Option 1",
    command=lambda: update_check_status(myRadioVar, 'radio')
).pack()

Radiobutton(
    root,
    text="Option 2",
    variable=myRadioVar,
    value="Option 2",
    command=lambda: update_check_status(myRadioVar, 'radio')
).pack()

# Entry box
myEntry = Entry(root)
myEntry.pack()
myEntry.bind("<KeyRelease>", entryEvent)

# Listbox
myListBox = Listbox(root)
for item in ["First", "Second", "Third"]:
    myListBox.insert(END, item)
myListBox.pack()
myListBox.bind("<<ListboxSelect>>", listBoxEvent)

# Buttons
Button(root, text="Exit Button", command=root.quit).pack()

toggle = Button(root, text='ON', command=button_toggle)
toggle.pack()

root.mainloop()
