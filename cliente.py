import xmlrpc.client
import cryptocode as cc

setence = input("Digite o texto a ser criptografado: ")

with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
    encryptedText, password = proxy.encryptorText(setence)
    print("Texto criptografado: {}" .format(encryptedText))
    print(password)
    decryptedText = cc.decrypt(encryptedText, password)
    print("Texto descriptografado: {}" .format(decryptedText))