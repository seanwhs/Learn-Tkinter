from tkinter import *           # Import tkinter library
from PIL import ImageTk, Image  # Import Pillow for image handling

root = Tk()                     # Create main window
root.title('Introduction to Images')            # Set window title

icon = PhotoImage(file='./images/batman_icon.png')  # Load window icon
root.iconphoto(False, icon)     # Set window icon

myImage = ImageTk.PhotoImage(Image.open('./images/batman.jpg'))  # Load main image
myLabel = Label(image=myImage)  # Create label to display image
myLabel.pack()                  # Add label to window

button_quit = Button(root, text='Exit Program', command=root.quit)  # Create exit button
button_quit.pack()              # Add button to window

root.mainloop()                 # Run the GUI event loop
