'''
Nathan W.
2022-05-18

'''

# Imports
from tkinter import *
from tkinter.ttk import *
from time import strftime

# Create interface
root = Tk();
root.title("Clock")

# Get the time
def time():
    string = strftime("%I:%M:%S %p")
    label.config(text = string)
    label.after(1000, time)

label = Label(root, font=("DS-Digital", 80), background = "black", foreground = "green")
label.pack(anchor = "center")

# Call the time function
time()

# Run the Tkinter event loop
mainloop()



