from tkinter import *
def on_button_click():
    label.config(text="Hello World")

root = Tk()
Button(root, text="Press this button", command=on_button_click).pack()
label = Label(root)
label.pack()
root.mainloop()
