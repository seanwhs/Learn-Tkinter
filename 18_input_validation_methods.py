# ------------------------ Validation Methods Demonstrated
# 1️⃣ Button-triggered validation (Vowel Entry)
# 2️⃣ key-based validatecommand (Number Entry)
# 3️⃣ focusout validatecommand + invalidcommand (Palindrome Entry)

from tkinter import *
from tkinter import ttk
import random

root = Tk()
root.title("Validation Example")

# ------------------------ Styling
s = ttk.Style()
s.layout("Frame.IFrame", [("Frame.background", {"sticky": "nsew"})])
s.configure("Frame.IFrame", background="#94B49F")

# ------------------------- Main Frame
mainFrame = ttk.Frame(root, style='Frame.IFrame', width=400, height=250)
mainFrame.grid(row=0, column=0, sticky='NEWS')

# ------------------------- Callback Functions

# --- Vowel validation ---
def isVowel():
    text = entry1.get().lower().strip()
    if len(text) == 0:
        status1.config(text='...Still waiting')
    elif len(text) > 1:
        status1.config(text='Only ONE character!')
    elif text in 'aeiou':
        status1.config(text='Correct!')
    else:
        status1.config(text='Incorrect!')

# --- Number validation ---
def isNumber(new_text):
    """Check if Entry2 contains only digits."""
    if new_text == "":
        status2.config(text='...waiting for input')
    elif new_text.isdigit():
        status2.config(text='Correct!')
    else:
        status2.config(text='Incorrect!')
    return True  # Always True to allow edits/deletion

# --- Palindrome validation ---
def checkPalindrome():
    """Return True if palindrome, False otherwise."""
    text = entry3.get().lower().strip()
    if text == "":
        status3.config(text="...Still Waiting")
        return True
    if text == text[::-1]:
        status3.config(text="Nice Palindrome!")
        return True
    else:
        return False  # triggers invalidcommand

def proposePalindrome():
    """Suggest a random palindrome if invalid."""
    palindromes = ['anna', 'civic', 'kayak', 'level', 'mom', 'racecar',
                   'radar', 'rotator', 'sagas', 'solos', 'wow']
    status3.config(text=f"Try this: {random.choice(palindromes)}")

# ------------------------- Register validatecommand
num_vcmd = (root.register(isNumber), '%P')
pal_vcmd = (root.register(checkPalindrome),)

# ------------------------- Layout

# Vowel Entry
Label(mainFrame, text='1. Enter a vowel:', font=('Helvetica', 10, 'bold'), bg='#94B49F').grid(row=0, column=0, pady=10, padx=10, sticky='WE')
entry1 = Entry(mainFrame)
entry1.grid(row=0, column=1, pady=10, padx=10, sticky='WE')
Button(mainFrame, text='Validate', command=isVowel).grid(row=0, column=2, pady=10, padx=10, sticky='WE')
status1 = Label(mainFrame, text='...waiting for input', bg='#94B49F')
status1.grid(row=0, column=3, pady=10, padx=10, sticky='WE')

# Number Entry
Label(mainFrame, text='2. Enter a number:', font=('Helvetica', 10, 'bold'), bg='#94B49F').grid(row=1, column=0, pady=10, padx=10, sticky='WE')
entry2 = Entry(mainFrame, validate='key', validatecommand=num_vcmd)
entry2.grid(row=1, column=1, pady=10, padx=10, sticky='WE')
status2 = Label(mainFrame, text='...waiting for input', bg='#94B49F')
status2.grid(row=1, column=3, pady=10, padx=10, sticky='WE')

# Palindrome Entry
Label(mainFrame, text='3. Enter a palindrome:', font=('Helvetica', 10, 'bold'), bg='#94B49F').grid(row=2, column=0, pady=10, padx=10, sticky='WE')
entry3 = Entry(mainFrame, validate='focusout', validatecommand=pal_vcmd, invalidcommand=proposePalindrome)
entry3.grid(row=2, column=1, pady=10, padx=10, sticky='WE')
status3 = Label(mainFrame, text='...waiting for input', bg='#94B49F')
status3.grid(row=2, column=3, pady=10, padx=10, sticky='WE')

# ------------------------- Grid expansion
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainFrame.columnconfigure(0, weight=1)
mainFrame.columnconfigure(1, weight=1)

root.mainloop()
