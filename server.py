from xmlrpc.server import SimpleXMLRPCServer
import cryptocode as cc

senha = "superSenha"
server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")

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
