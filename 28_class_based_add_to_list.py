from tkinter import *
from tkinter import ttk

def main():
    app = Application('Demo:: Class Based App to Add User Input to a List')
    
    # Exit button at the bottom, spans both columns
    btnExit = Button(app, text='Exit Program', command=app.quit)
    btnExit.grid(row=1, column=0, columnspan=2, sticky='ew', padx=5, pady=5)
    
    # Make exit button stick to bottom when window resizes
    app.rowconfigure(1, weight=0)

    app.mainloop()  # Run the app

class Application(Tk):
    def __init__(self, title_name):
        super().__init__()
        self.title(title_name)  # Window title

        # Two equal-width columns for two input forms
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)  # Form row expands

        # Left input form
        frame = InputForm(self)
        frame.grid(row=0, column=0, sticky='nsew')

        # Right input form
        frame2 = InputForm(self)
        frame2.grid(row=0, column=1, sticky='nsew')

class InputForm(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Columns: entry, add button, scrollbar
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        self.columnconfigure(2, weight=0)
        self.rowconfigure(1, weight=1)  # Listbox row expands

        # Entry field for input
        self.entry1 = ttk.Entry(self)
        self.entry1.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
        self.entry1.bind('<Return>', self.addToList)  # Add on Enter key

        # Add button next to entry
        self.btnAdd = Button(self, text='Add to List', command=self.addToList)
        self.btnAdd.grid(row=0, column=1, padx=5, pady=5)

        # Listbox to display items
        self.listBox = Listbox(self)
        self.listBox.grid(row=1, column=0, columnspan=2, sticky='nsew', padx=(5, 0), pady=5)

        # Vertical scrollbar
        scroll = Scrollbar(self, orient=VERTICAL, command=self.listBox.yview)
        scroll.grid(row=1, column=2, sticky='ns', padx=(0, 5), pady=5)
        self.listBox.config(yscrollcommand=scroll.set)

        # Clear button below listbox
        btnClear = Button(self, text='Clear List Box', command=lambda: self.listBox.delete(0, END))
        btnClear.grid(row=2, column=0, sticky='ew', padx=5, pady=5)

    def addToList(self, event=None):
        """Add entry text to listbox and clear entry"""
        text = self.entry1.get()
        if text:
            self.listBox.insert(END, text)
            self.entry1.delete(0, END)

if __name__ == '__main__':
    main()
