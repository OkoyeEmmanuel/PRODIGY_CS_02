from logging import root
from tkinter import *
from tkinter import filedialog

root = Tk()
root.withdraw()  

def encrypt_image(key):
    global filename
    global image
    filename = filedialog.askopenfilename(initialdir="/", title="Select an image to encrypt", filetypes=(("png files","*.png"), ("jpeg files","*.jpeg"),("jpg files","*.jpg"), ("all files","*.*")))
    file_binary =  open(filename, 'rb') # open the file in binary mode, rb = read binary

    image = file_binary.read() 

    file_binary.close()
    image = bytearray(image) 

    root.destroy()
    for index, values in enumerate(image):
        image[index] = values ^ key
    

    file_binary = open(filename, 'wb') 
    file_binary.write(image)
    file_binary.close()
    print("Encryption done...")
     
   


    

def decrypt_image(key):
    global filename
    filename = filedialog.askopenfilename(initialdir="/", title="Select an image to decrypt", filetypes=(("png files","*.png"), ("jpeg files","*.jpeg"), ("all files","*.*")))
    print(filename)
    root.destroy()

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
        decryption_key = int(input("Enter encryption key: "))
        decrypt_image(decryption_key)
    elif choice == 3:
        bExit = True
        print("Exiting the program...")
    else:
        print("Invalid choice. Please try again.")
        

