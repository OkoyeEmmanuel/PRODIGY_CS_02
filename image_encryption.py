from logging import root
from tkinter import *
from tkinter import filedialog
from PIL import Image


root = Tk()
root.withdraw()  

def encrypt_image(key):
    global filename
    global image
    filename = filedialog.askopenfilename(initialdir="/", title="Select an image to encrypt", filetypes=(("png files","*.png"), ("jpeg files","*.jpeg"),("jpg files","*.jpg"), ("all files","*.*")))
    image = Image.open(filename)
    pixels = image.load()
    width, height = image.size
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256

            pixels[i, j] = (r, g, b)
    image.save("encrypted_image.png")
   
     
   


    

def decrypt_image(key):
    global filename
    filename = filedialog.askopenfilename(initialdir="/", title="Select an image to decrypt", filetypes=(("png files","*.png"), ("jpeg files","*.jpeg"),("jpg files","*.jpg"), ("all files","*.*")))

    



bExit = False

while not bExit:
    print("=============================================")
    print("Welcome to Image Encryption Program")
    print("=============================================")
    print("1. Encrypt an image")
    print("2. Decrypt an image")
    print("3. Exit")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        encryption_key = int(input("Enter encryption key: "))
        encrypt_image(encryption_key)
    elif choice == 2:
        decryption_key = int(input("Enter decryption key: "))
        decrypt_image(decryption_key)
    elif choice == 3:
        bExit = True
        print("Exiting the program...")
    else:
        print("Invalid choice. Please try again.")
        

