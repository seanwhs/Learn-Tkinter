# 🐍 **Tkinter Tutorial: Build a Simple GUI Application**

Tkinter is Python’s built-in library for creating desktop applications. It is lightweight, easy to learn, and perfect for beginners.

---

# ⭐ 1. What is Tkinter?

Tkinter is a Python package that provides a set of GUI (Graphical User Interface) tools such as:

* Buttons
* Labels
* Text boxes
* Frames
* Menus
* etc.

You do **not** need to install anything—Tkinter comes with Python.

To verify Tkinter is installed:

```python
import tkinter
print(tkinter.TkVersion)
```

If no error occurs, you're ready!

---

# ⭐ 2. Tkinter’s Basic Structure

Every Tkinter app follows this pattern:

```python
import tkinter as tk

root = tk.Tk()      # Create main window
root.mainloop()     # Start the event loop
```

Inside the window, you add widgets (buttons, labels, etc.) and arrange them with geometry managers like:

* `.pack()`
* `.grid()`
* `.place()`

---

# ⭐ 3. Widgets You Should Know

### **Label**

Displays text:

```python
label = tk.Label(root, text="Hello")
label.pack()
```

### **Button**

Triggers an action:

```python
def on_click():
    print("Button clicked!")

button = tk.Button(root, text="Click Me", command=on_click)
button.pack()
```

### **Entry**

Single-line text input:

```python
entry = tk.Entry(root)
entry.pack()
```

### **StringVar**

Variable that updates widgets dynamically:

```python
name = tk.StringVar()
entry = tk.Entry(root, textvariable=name)
```

---

# ⭐ 4. Layout Management (pack, grid)

### **pack()** – simple, good for vertical stacking

### **grid()** – table-style layout

(You cannot mix pack and grid in the same parent widget!)

---

# 🎉 5. COMPLETE EXAMPLE APPLICATION

## ✔ A Simple “Name Greeter App” (Perfect for Learning Tkinter)

**Features:**

* Input box
* Button
* Dynamic message update
* Basic layout with `.grid()`
* Uses `StringVar()`

---

## 🚀 Full Code

```python
import tkinter as tk

def main():
    # Create main window
    root = tk.Tk()
    root.title("Tkinter Greeter App")
    root.geometry("350x200")

    # Title label
    title_label = tk.Label(root, text="Welcome to Tkinter!", font=("Arial", 16))
    title_label.grid(row=0, column=0, columnspan=2, pady=10)

    # Label + Entry
    name_label = tk.Label(root, text="Enter your name:")
    name_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

    name_var = tk.StringVar()
    name_entry = tk.Entry(root, textvariable=name_var)
    name_entry.grid(row=1, column=1, padx=10, pady=5)

    # Output Label
    output_var = tk.StringVar()
    output_label = tk.Label(root, textvariable=output_var, font=("Arial", 12), fg="blue")
    output_label.grid(row=3, column=0, columnspan=2, pady=10)

    # Button action
    def greet():
        name = name_var.get().strip()
        if name:
            output_var.set(f"Hello, {name}! 👋")
        else:
            output_var.set("Please enter your name.")

    # Button
    greet_button = tk.Button(root, text="Greet Me", command=greet)
    greet_button.grid(row=2, column=0, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
```

---

# 🧠 6. Explanation of Key Concepts Used

### ✔ **root = tk.Tk()**

Creates the main application window.

### ✔ **StringVar()**

Stores a string value and updates widgets automatically.

### ✔ **grid()**

Arranges widgets in rows and columns.

### ✔ **command=greet**

Connects the button to a function.

### ✔ **root.mainloop()**

Starts Tkinter’s event loop (keeps the window open).




