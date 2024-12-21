import os
import pyaes

file_name = "teste.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

key = b'0123456789abcdef'
aes = pyaes.AESModeOfOperationCTR(key)
encrypted_data = aes.encrypt(file_data)

os.remove(file_name)

new_file = 'teste.txt.enc'
new_file = open(new_file, "wb")
new_file.write(encrypted_data)
new_file.close()