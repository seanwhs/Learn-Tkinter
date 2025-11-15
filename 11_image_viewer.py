from tkinter import *
from PIL import Image, ImageTk

# --- Configuration ---
TARGET_SIZE = (400, 300)
IMAGE_PATHS = [
    './images/Avengers1.png',
    './images/Avengers2.png',
    './images/batman.jpg',
    './images/black-panther.png',
    './images/superman.png',
    './images/sup1.webp'
]

# --- Functions ---
def load_and_resize(path, size):
    """Load an image from disk and resize it."""
    image = Image.open(path).resize(size, Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(image)

def show_image(index):
    """Display image at the given index and update button states."""
    global current_index

    current_index = index
    image_label.config(image=images[current_index])

    # Enable/disable navigation buttons based on current image
    back_button.config(state=NORMAL if current_index > 0 else DISABLED)
    forward_button.config(state=NORMAL if current_index < len(images) - 1 else DISABLED)

def next_image():
    """Go to the next image."""
    if current_index < len(images) - 1:
        show_image(current_index + 1)

def prev_image():
    """Go to the previous image."""
    if current_index > 0:
        show_image(current_index - 1)

# --- Main Window Setup ---
root = Tk()
root.title("Image Viewer")

icon = PhotoImage(file='./images/batman_icon.png')
root.iconphoto(False, icon)

# --- Load all images once ---
images = [load_and_resize(path, TARGET_SIZE) for path in IMAGE_PATHS]

# --- UI Setup ---
image_label = Label(root)
image_label.grid(row=0, column=0, columnspan=3, padx=40, pady=40)

back_button = Button(root, text='<<', command=prev_image)
quit_button = Button(root, text='Exit Program', command=root.quit)
forward_button = Button(root, text='>>', command=next_image)

back_button.grid(row=1, column=0)
quit_button.grid(row=1, column=1)
forward_button.grid(row=1, column=2)

# --- Start with first image ---
current_index = 0
show_image(current_index)

# --- Run App ---
root.mainloop()
