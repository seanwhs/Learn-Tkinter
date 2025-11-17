from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Combobox Example")
root.geometry("300x150")

# Label prompting user
Label(root, text="Select a fruit:", font=("Arial", 12)).pack(pady=10)

# Combobox with predefined fruits (readonly prevents typing)
fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
combo = ttk.Combobox(root, values=fruits, state="readonly")
combo.pack(pady=5)

# Label to display current selection
selected_label = Label(root, text="Selected: None", font=("Arial", 10), fg="blue")
selected_label.pack(pady=10)

# Function to update label when selection changes
def show_selection(event=None):
    selected_label.config(text=f"Selected: {combo.get()}")

# Bind combobox selection event to function
combo.bind("<<ComboboxSelected>>", show_selection)

root.mainloop()
