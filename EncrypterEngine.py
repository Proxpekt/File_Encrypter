from cryptography.fernet import Fernet
import os

def generate_Key():
    key = Fernet.generate_key()

    with open("secret.key", "wb") as keyFile:
        keyFile.write(key)

def load_Key():
    return open("secret.key", "rb").read()


def encrypt_File(filePath,key):
    f = Fernet(key)

    with open(filePath, "rb") as file:
        fileData = file.read()
    
    encryptedData = f.encrypt(fileData)

    with open(filePath, "wb") as file:
        file.write(encryptedData)

def decrypt_File(filePath, key):
    f = Fernet(key)

    with open(filePath, "rb") as file:
        encryptedData = file.read()

    fileData = f.decrypt(encryptedData)

    with open(filePath, "wb") as file:
        file.write(fileData)


def encrypt_Folder(folderPath, key):
    for root, dirs, files in os.walk(folderPath):
        for file in files:
            filePath = os.path.join(root, file)
            encrypt_File(filePath,key)
            print(f"The {file} is encrypted")

def decrypt_Folder(folderPath, key):
    for root, dirs, files in os.walk(folderPath):
        for file in files:
            filePath = os.path.join(root, file)
            decrypt_File(filePath,key)
            print(f"The {file} is decrypted")



answer = input("What may I help you with?\n1. Encryption\n2. Decryption\n")
priority = "high"

if(answer=="1" and priority=="high"):
    generate_Key()
    key = load_Key()
    folder = r"C:\Users\aayus\OneDrive\Desktop\Prozpekt\Aayu\Saundriya Sabun Nirma"
    encrypt_Folder(folder, key)
else:
    key = load_Key()
    folder = r"C:\Users\aayus\OneDrive\Desktop\Prozpekt\Aayu\Saundriya Sabun Nirma"
    decrypt_Folder(folder, key)




