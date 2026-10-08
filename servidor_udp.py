import socket 

if __name__ == "__main__":

  IP_VM = "192.168.64.2" # amandis 192.168.64.2
                         # dani 10.0.2.15
  server_address = (IP_VM, 8000)
  buff_size = 16                         

  server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  server_socket.bind(server_address)

  while True: 
    message, address = server_socket.recvfrom(buff_size)
    print(message.decode(), end="", flush=True)

