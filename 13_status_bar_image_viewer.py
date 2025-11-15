from tkinter import *
from PIL import Image, ImageTk

# App settings
TARGET_SIZE = (400, 300)
IMAGE_PATHS = [
    './images/Avengers1.png',
    './images/Avengers2.png',
    './images/batman.jpg',
    './images/black-panther.png',
    './images/superman.png',
    './images/sup1.webp',
    './images/spiderman.jpg',
    './images/spiderman2.jpg',
    './images/hulk.jpg',
    './images/flash.jpg'
]

def load_and_resize(path, size):
    """Load an image and resize it to the given size."""
    image = Image.open(path).resize(size, Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(image)

def show_image(index):
    """Display the image at the given index and update controls."""
    global current_index
    current_index = index

    image_label.config(image=images[current_index])
    status_label.config(text=f'Image {current_index + 1} of {len(images)}')

    back_button.config(state=NORMAL if current_index > 0 else DISABLED)
    forward_button.config(state=NORMAL if current_index < len(images) - 1 else DISABLED)

def next_image():
    """Show the next image."""
    if current_index < len(images) - 1:
        show_image(current_index + 1)

def prev_image():
    """Show the previous image."""
    if current_index > 0:
        show_image(current_index - 1)

# Main window
root = Tk()
root.title("Image Viewer")
root.iconphoto(False, PhotoImage(file='./images/batman_icon.png'))

# Load all images with list comprehension
images = [load_and_resize(path, TARGET_SIZE) for path in IMAGE_PATHS]

# Image display area
image_label = Label(root)
image_label.grid(row=0, column=0, columnspan=3, padx=40, pady=40)

# Status bar (updated dynamically)
status_label = Label(root, bd=1, relief=SUNKEN, anchor=E)
status_label.grid(row=2, column=0, columnspan=3, sticky=W+E)

# Navigation buttons
back_button = Button(root, text='<<', command=prev_image)
quit_button = Button(root, text='Exit Program', command=root.quit)
forward_button = Button(root, text='>>', command=next_image)

back_button.grid(row=1, column=0)
quit_button.grid(row=1, column=1)
forward_button.grid(row=1, column=2, pady=10)

# Initialize app
current_index = 0
show_image(current_index)

root.mainloop()
