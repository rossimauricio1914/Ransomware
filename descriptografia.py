import os
import pyaes

## Abrindo o arquivo criptografado
file_name = "texto.txt.crypt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## Chave de descriptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## Remover o arquivo descriptografado
os.remove(file_name)

## Criando o arquivo descriptografado
new_file = "texto.txt"
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()
