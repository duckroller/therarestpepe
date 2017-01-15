import os
import sys

def getDestinationFolder():
    folders = {"Settings"}
    for folder in folders:
    
file_name = "rarest_meme.png"
destination_folder = "/media/pi/DISK_IMG"

#Encrypt the file
def encrypt(file_name):
    print("Encryting the files...")
    try:
        os.system("gpg -r Ahsan --encrypt " + file_name)
        os.remove(file_name)
    except:
        print("Cannot encrypt the file.")
    print("File successfully encrypted. You now have the rarest meme.")

#Get the name of the encrypted file
def getEncryptedFile(file_name):
    return file_name + ".gpg"

#Move the encrypted file into the destination folder
def moveFile(file_name):
    encryptedFile = file_name + ".gpg"
    os.system("mv " + encryptedFile + " " + destination_folder)

encrypt(file_name)
moveFile(getEncryptedFile(file_name))
