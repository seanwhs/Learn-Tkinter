from tkinter import *

root = Tk()
root.title("Tkinter .config() Examples")
root.geometry("400x600")

# ------------------------------
# 1. Label Example
# ------------------------------
label = Label(root, text="Original Label", fg="black")
label.pack(pady=10)

# Change label config
label.config(text="Updated Label", fg="blue", bg="yellow", font=("Arial", 14))


# ------------------------------
# 2. Button Example
# ------------------------------
def say_hi():
    print("Hi!")

button = Button(root, text="Original Button")
button.pack(pady=10)

# Change button config
button.config(text="Click Me", command=say_hi)


# ------------------------------
# 3. Entry Example
# ------------------------------
entry = Entry(root)
entry.pack(pady=10)

entry.config(width=35)
entry.insert(0, "Default entry text")


# ------------------------------
# 4. Frame Example
# ------------------------------
frame = Frame(root, width=200, height=80, bg="lightgray")
frame.pack(pady=15)

# Update frame settings
frame.config(bg="lightgreen", width=250, height=100)


# ------------------------------
# 5. Text Widget Example
# ------------------------------
text_widget = Text(root, height=4, width=30)
text_widget.pack(pady=10)

text_widget.config(bg="black", fg="white", font=("Courier", 12))
text_widget.insert("end", "This is a Text widget\nwith updated config.")


# ------------------------------
# 6. Disable/Enable Example
# ------------------------------
disable_button = Button(root, text="I am disabled")
disable_button.pack(pady=10)

disable_button.config(state="disabled")


# ------------------------------
# 7. Print Configuration Example
# ------------------------------
def print_label_config():
    print(label.config())  # prints all config options for the label

show_config_btn = Button(root, text="Print Label Config", command=print_label_config)
show_config_btn.pack(pady=10)


root.mainloop()
