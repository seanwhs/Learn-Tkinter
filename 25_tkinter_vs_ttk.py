from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Tkinter vs ttk Comparison")
root.geometry("600x450")

# ------------------------ Styling for ttk widgets
style = ttk.Style()
style.theme_use("default")  # Use default ttk theme
style.configure("My.TButton", font=("Arial", 11))  # Custom button style
style.configure("My.TLabel", font=("Arial", 11))   # Custom label style

# ------------------------ Section Titles
Label(root, text="Native Tkinter Widgets", font=("Arial", 16, "bold")).grid(row=0, column=0, pady=10)
Label(root, text="ttk (Themed Tkinter) Widgets", font=("Arial", 16, "bold")).grid(row=0, column=1, pady=10)

# =============================== NATIVE TKINTER ===============================
Label(root, text="TK Label", bg="lightblue", relief="solid", font=("Arial", 12)).grid(row=1, column=0, pady=5, padx=10)
Entry(root, bg="yellow", relief="sunken", bd=3).grid(row=2, column=0, pady=5, padx=10)
Button(root, text="TK Button", bg="lightgreen", fg="black", relief="raised", bd=4).grid(row=3, column=0, pady=5, padx=10)
Checkbutton(root, text="TK Checkbutton", bg="white").grid(row=4, column=0, pady=5, padx=10)
Radiobutton(root, text="TK Radiobutton", bg="white", value=1).grid(row=5, column=0, pady=5, padx=10)

# =============================== TTK WIDGETS ===============================
ttk.Label(root, text="ttk Label", style="My.TLabel").grid(row=1, column=1, pady=5, padx=10)
ttk.Entry(root).grid(row=2, column=1, pady=5, padx=10)
ttk.Button(root, text="ttk Button", style="My.TButton").grid(row=3, column=1, pady=5, padx=10)
ttk.Checkbutton(root, text="ttk Checkbutton").grid(row=4, column=1, pady=5, padx=10)
ttk.Radiobutton(root, text="ttk Radiobutton", value=1).grid(row=5, column=1, pady=5, padx=10)

# -------------------- ttk-only widgets --------------------
ttk.Label(root, text="(Widgets below only exist in ttk)").grid(row=6, column=1, pady=(20,5))

# Combobox (dropdown selection)
ttk.Combobox(root, values=["Red", "Green", "Blue"]).grid(row=7, column=1, pady=5)

# Progressbar (loading bar)
ttk.Progressbar(root, length=150).grid(row=8, column=1, pady=5)

# Treeview (table-like widget)
tree = ttk.Treeview(root, height=3)
tree['columns'] = ("Name", "Age")
tree.column("#0", width=0, stretch=NO)  # Hide default first column
tree.column("Name", width=100)
tree.column("Age", width=40)
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")
tree.insert("", "end", values=("Alice", 30))
tree.insert("", "end", values=("Bob", 25))
tree.insert("", "end", values=("Charlie", 40))
tree.grid(row=9, column=1, pady=10)

root.mainloop()
