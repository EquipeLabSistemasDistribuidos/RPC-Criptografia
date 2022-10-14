import xmlrpc.client

servidor = input("Servidor: ")
setence = input("Digite o texto a ser criptografado: ")

try:
    with xmlrpc.client.ServerProxy("http://"+servidor+":1234/") as proxy:
        encryptedText = proxy.encryptorText(setence)
        print("Texto criptografado: {}" .format(encryptedText))

        decryptedText = proxy.decryptorText(encryptedText)
        print("Texto descriptografado: {}" .format(decryptedText))

except Exception as e:
    print(e)