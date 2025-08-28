from tkinter import *
from tkinter import filedialog

root = Tk()
root.geometry("400x400") # the box size, GUI


def encrypt_image(): 
   print("Image")

button = Button(root, text="Select to encrypt an image", command=encrypt_image)
button.place(x=100, y=100)



root.mainloop() 