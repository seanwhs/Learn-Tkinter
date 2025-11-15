from tkinter import *

def draw_rectangle():
    # Draw a blue rectangle
    canvas.create_rectangle(50, 50, 150, 150, fill='blue')

def draw_circle():
    # Draw a red circle
    canvas.create_oval(50, 50, 150, 150, fill='red')

def draw_line():
    # Draw a green line
    canvas.create_line(50, 50, 150, 150, fill='green')

def clear_canvas():
    # Clear the canvas
    canvas.delete('all')

# Main window
root = Tk()
root.title('Canvas Drawing Example')

# Drawing canvas
canvas = Canvas(root, width=400, height=300, bg='white')
canvas.pack()

# Action buttons
Button(root, text='Draw Rectangle', command=draw_rectangle, bg='light blue').pack(side='left', padx=5)
Button(root, text='Draw Circle', command=draw_circle, bg='pink').pack(side='left', padx=5)
Button(root, text='Draw Line', command=draw_line, bg='light green').pack(side='left', padx=5)
Button(root, text='Clear', command=clear_canvas, bg='beige').pack(side='left', padx=5)
Button(root, text='Exit Program', command=root.quit, bg='red').pack(side='left', padx=5)

root.mainloop()
