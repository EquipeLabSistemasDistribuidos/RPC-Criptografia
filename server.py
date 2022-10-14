from xmlrpc.server import SimpleXMLRPCServer
import cryptocode as cc
import get_ip as gip

#Obtendo IP da máquina atual
IP = gip.get_ip()
print(IP)

senha = "superSenha"
server = SimpleXMLRPCServer((IP, 1234))
print("Listening on port 1234...")

def encryptorText(value):
    print("----------------------------------------------")
    print("Requisição recebida com o seguinte argumento: " + str(value))
    textEncrypted = cc.encrypt(value, senha)
    print("Texto criptografado: {}" .format(textEncrypted))
    print("----------------------------------------------")
    return textEncrypted

def decryptorText(value):
    print("----------------------------------------------")
    print("Requisição recebida com o seguinte argumento: " + str(value))
    textDecrypted = cc.decrypt(value, senha)
    print("Texto descriptografado: {}" .format(textDecrypted))
    print("----------------------------------------------")
    return textDecrypted

server.register_function(encryptorText, "encryptorText")
server.register_function(decryptorText, "decryptorText")

try:
    print("Control-C to exit server")
    server.serve_forever()
except KeyboardInterrupt:
    print ("Exiting server...")
