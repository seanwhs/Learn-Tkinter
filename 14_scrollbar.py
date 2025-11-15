from tkinter import *
from tkinter import scrolledtext

# --- Functions ---
def insert_text():
    """Insert sample text into ScrolledText and update label."""
    message = 'The quick brown fox jumped over the lazy dog.'
    text.insert(END, message)
    info_label.config(text=f'You entered: {message}')

def show_text(event=None):
    """Update label dynamically as user types."""
    entered = text.get('1.0', END).strip()
    info_label.config(text=f'You entered: {entered}')

def clear_scroll_and_label():
    """Clear both ScrolledText and info label."""
    text.delete('1.0', END)
    info_label.config(text='')


# --- Main Window ---
root = Tk()
root.title('Scrollbar Example')

# ScrolledText widget
text = scrolledtext.ScrolledText(root, wrap=WORD, width=40, height=10)
text.pack(padx=10, pady=10)
text.bind('<KeyRelease>', show_text)  # update label on key release

# Buttons
Button(root, text='Insert Text', command=insert_text).pack(padx=5, pady=5)
Button(root, text='Clear', command=clear_scroll_and_label).pack(padx=5, pady=5)
Button(root, text='Exit', command=root.quit).pack(padx=5, pady=5)

# Dynamic label for live updates
info_label = Label(root, text="")
info_label.pack(padx=5, pady=5)

root.mainloop()
