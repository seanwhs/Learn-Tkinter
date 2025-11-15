from tkinter import *

root = Tk()

# Toggle button text between ON and OFF
def toggle():
    button1['text'] = 'OFF' if button1['text'] == 'ON' else 'ON'

# Frames with padding and different styles
frame1 = Frame(root, padx=200, pady=50, bg='light blue', borderwidth=5, relief=SUNKEN)
frame1.pack()

frame2 = Frame(root, padx=200, pady=50, bg='pink', relief=RAISED)
frame2.pack()

# Labels inside each frame
Label(frame1, text='Sits in Frame1').pack()
Label(frame2, text='Sits in Frame2').pack()

# Toggle button inside frame1
button1 = Button(frame1, text='ON', command=toggle)
button1.pack(pady=30)

# Exit button inside frame2
Button(frame2, text='Exit', command=root.quit).pack(pady=5)

root.mainloop()
