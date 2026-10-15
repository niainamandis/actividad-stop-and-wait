from SocketTCP import SocketTCP

address = ("10.0.2.15", 8000)
server_socketTCP = SocketTCP()
server_socketTCP.bind(address)
print("Esperando conexión...")
connection_socketTCP, new_address = server_socketTCP.accept()
print(f"Conexión establecida con éxito en {new_address}!")
