from opcode import opname
from cryptography.fernet import Fernet
import os 

files = []

for file in os.listdir():
    if(file == "encrypt.py" or file == 'keyfile.txt' or file == 'decrypt.py'):
        continue
    files.append(file)
    with open('keyfile.txt','rb') as keyfile:
        secret_key = keyfile.read()
    for file in files:
        with open(file,'rb') as f:
            content = f.read()
        with open(file,'wb') as f:
            decrypted_content  = Fernet(secret_key).decrypt(content)
            f.write(decrypted_content)

print('All the files in this directory were decrypted')

