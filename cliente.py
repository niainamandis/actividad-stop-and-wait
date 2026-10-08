import socket 

if __name__ == "__main__":
  
  ruta = input()                      

  with open(ruta, "rb") as f:      
    data = f.read()

  IP_VM = "192.168.64.2" # amandis 192.168.64.2
                         # dani 10.0.2.15
  server_address = (IP_VM, 8000)
  buff_size = 16 

  client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

  for i in range(0, len(data), 16):
    client_socket.sendto(data[i:i+16], server_address)

  client_socket.close()
