# 🎓 **Tkinter Tutorial: Multi-Page GUI with `ttk.Notebook`**

## 🌟 What You’ll Learn

* What `ttk.Notebook` is
* How to use Frames as "pages"
* How to place widgets inside each page
* How to switch between pages
* How to structure a multi-file Tkinter project

By the end, you’ll have a **tabbed interface** like:

```
+----------------------------+
| Home | Settings | About   |
+----------------------------+
```

---

# 🧩 1. What is `ttk.Notebook`?

`ttk.Notebook` is a widget from the `ttk` (Themed Tk) module.
It creates a **tab control**, where each tab shows a different frame.

You can think of it like:

```
Notebook  → contains many Frames
Frame     → contains widgets (labels, buttons, etc.)
```

This is the foundation of multi-page Tkinter applications.

---

# 🧩 2. Basic Structure

The minimal code to create a Notebook:

```python
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

root.mainloop()
```

But this creates an empty tab control—so next, we add frames.

---

# 🧩 3. Frames as Notebook Pages

Each Notebook tab is just a Frame:

```python
home_page = ttk.Frame(notebook)
settings_page = ttk.Frame(notebook)
about_page = ttk.Frame(notebook)

notebook.add(home_page, text="Home")
notebook.add(settings_page, text="Settings")
notebook.add(about_page, text="About")
```

Now we can put widgets *inside those frames*.

---

# 🚀 4. Complete Multi-Page Application

The app includes:

* **Home tab:** A welcome message
* **Settings tab:** Simple settings controls
* **About tab:** App description

---

## ⭐ Full Working Code

```python
import tkinter as tk
from tkinter import ttk


class MultiPageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter Multi-Page App")
        self.root.geometry("500x300")

        # --- Create Notebook ---
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill="both")

        # --- Create Pages ---
        self.create_home_page()
        self.create_settings_page()
        self.create_about_page()

    # -----------------------------------------------------------
    # Home Page
    # -----------------------------------------------------------
    def create_home_page(self):
        home = ttk.Frame(self.notebook)
        self.notebook.add(home, text="Home")

        title = ttk.Label(home, text="🏠 Welcome to the Multi-Page App!", font=("Arial", 16))
        title.pack(pady=20)

        description = ttk.Label(
            home,
            text="Use the tabs above to explore different pages.",
            font=("Arial", 12)
        )
        description.pack(pady=10)

        btn = ttk.Button(home, text="Go to Settings",
                         command=lambda: self.notebook.select(1))
        btn.pack(pady=20)

    # -----------------------------------------------------------
    # Settings Page
    # -----------------------------------------------------------
    def create_settings_page(self):
        settings = ttk.Frame(self.notebook)
        self.notebook.add(settings, text="Settings")

        label = ttk.Label(settings, text="⚙ Settings", font=("Arial", 16))
        label.pack(pady=20)

        # Example option: change theme colors (dummy example)
        color_label = ttk.Label(settings, text="Choose a color theme:")
        color_label.pack(pady=5)

        theme_var = tk.StringVar(value="Light")

        light_radio = ttk.Radiobutton(settings, text="Light", variable=theme_var, value="Light")
        dark_radio = ttk.Radiobutton(settings, text="Dark", variable=theme_var, value="Dark")

        light_radio.pack()
        dark_radio.pack()

        save_btn = ttk.Button(settings, text="Save Settings", command=lambda: print("Theme:", theme_var.get()))
        save_btn.pack(pady=20)

    # -----------------------------------------------------------
    # About Page
    # -----------------------------------------------------------
    def create_about_page(self):
        about = ttk.Frame(self.notebook)
        self.notebook.add(about, text="About")

        label = ttk.Label(about, text="📘 About This App", font=("Arial", 16))
        label.pack(pady=20)

        message = ttk.Label(
            about,
            text=(
                "This multi-page GUI uses ttk.Notebook.\n"
                "Each tab is a Frame containing its own widgets.\n"
                "This structure helps keep large apps organized."
            ),
            justify="center"
        )
        message.pack(pady=10)


# -----------------------------------------------------------
# MAIN APP START
# -----------------------------------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = MultiPageApp(root)
    root.mainloop()
```

---

# 🎉 5. Concepts Explained for Beginners

### ✔ **Class-based structure**

We wrap the interface in a class:

```python
class MultiPageApp:
```

This keeps code organized and expandable.

---

### ✔ **Notebook**

The tab control:

```python
self.notebook = ttk.Notebook(root)
self.notebook.pack()
```

---

### ✔ **Frames as pages**

```python
page = ttk.Frame(self.notebook)
self.notebook.add(page, text="Home")
```

Each page is independent—great for big apps.

---

### ✔ **Navigation between tabs**

You can switch tabs programmatically:

```python
self.notebook.select(1)   # go to second tab
```

---

### ✔ **Widget placement**

We use `.pack()` for simplicity:

* `pack()` is easiest
* `grid()` is more precise
* Don’t mix grid and pack in the *same* frame

---

### ✔ **Using Variables**

Settings page uses a Tkinter variable:

```python
theme_var = tk.StringVar(value="Light")
```

`Radiobutton`s update this variable automatically.


