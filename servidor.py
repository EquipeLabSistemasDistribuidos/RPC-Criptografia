from msilib.schema import TextStyle
from xmlrpc.server import SimpleXMLRPCServer
import cryptocode as cc

senha = "superSenha"
server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")

def encryptorText(value):
    print("Requisição recebida com o seguinte argumento: " + str(value))
    textEncrypted = cc.encrypt(value, senha)
    print("Texto criptografado: {}" .format(textEncrypted))
    return textEncrypted, senha

server.register_function(encryptorText, "encryptorText")

try:
    print("Control-C to exit server")
    server.serve_forever()
except KeyboardInterrupt:
    print ("Exiting server...")