import socket 
from SocketTCP import SocketTCP

if __name__ == "__main__":
  
  ruta = input()                      

  with open(ruta, "rb") as f:      
    data = f.read()

  IP_VM = "192.168.64.2" # amandis 192.168.64.2
                         # dani 10.0.2.15
  server_address = (IP_VM, 8000)
  buff_size = 16 

  client_socket = SocketTCP()

  for i in range(0, len(data), 16):
    segment = {"SYN": 0, "ACK": 0, "FIN": 0, "SEQ": i, "DATOS": data[i:i+16]}
    client_socket.udp_socket.sendto(client_socket.create_segment(segment), server_address)

  client_socket.udp_socket.close()
