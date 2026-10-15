from SocketTCP import SocketTCP

address = ("10.0.2.15", 8000)
client_socketTCP = SocketTCP()
print("Conectando al servidor...")
client_socketTCP.connect(address)
print("Conectado con éxito!")
