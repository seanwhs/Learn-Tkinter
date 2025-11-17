from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Listbox vs Treeview Selection")
root.geometry("600x300")

# --------------------------- Sample Data ---------------------------
data = [
    ("Alice", 25),
    ("Bob", 30),
    ("Charlie", 40),
]

# --------------------------- LISTBOX (Tkinter) ---------------------------
Label(root, text="Listbox (Tkinter)", font=("Arial", 12, "bold")).grid(row=0, column=0, pady=10)
listbox = Listbox(root, width=25, height=6)
listbox.grid(row=1, column=0, padx=20)

# Add items to Listbox
for name, age in data:
    listbox.insert(END, f"{name} - {age}")

# Label to show selection
listbox_label = Label(root, text="Selected: None", fg="blue")
listbox_label.grid(row=2, column=0, pady=10)

# Function to update label when a Listbox item is selected
def show_listbox_selection(event=None):
    selection = listbox.get(ACTIVE)
    listbox_label.config(text=f"Selected: {selection}")

listbox.bind("<<ListboxSelect>>", show_listbox_selection)

# --------------------------- TREEVIEW (ttk) ---------------------------
Label(root, text="Treeview (ttk)", font=("Arial", 12, "bold")).grid(row=0, column=1, pady=10)
tree = ttk.Treeview(root, columns=("Name", "Age"), show="headings", height=6)
tree.grid(row=1, column=1, padx=20)

# Define headings
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")

# Add rows
for name, age in data:
    tree.insert("", END, values=(name, age))

# Label to show selection
tree_label = Label(root, text="Selected: None", fg="green")
tree_label.grid(row=2, column=1, pady=10)

# Function to update label when a Treeview item is selected
def show_treeview_selection(event=None):
    selected = tree.focus()
    if selected:
        values = tree.item(selected)["values"]
        tree_label.config(text=f"Selected: {values}")
    else:
        tree_label.config(text="Selected: None")

tree.bind("<<TreeviewSelect>>", show_treeview_selection)

root.mainloop()
