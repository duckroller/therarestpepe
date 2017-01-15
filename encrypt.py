import os
import sys

source_folders = {"Settings"}

def getDestinationFolder():
    result = ""
    print("ls -d */")
    for folder in sys.argv:
        if folder not in source_folders:
            result = folder
    return result        
    
file_name = "rarest_meme.png"
destination_folder = getDestinationFolder()

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
