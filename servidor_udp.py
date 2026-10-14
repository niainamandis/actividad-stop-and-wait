import socket 
from SocketTCP import SocketTCP

if __name__ == "__main__":

  IP_VM = "192.168.64.2" # amandis 192.168.64.2
                         # dani 10.0.2.15
  server_address = (IP_VM, 8000)

  server_socket = SocketTCP() 
  server_socket.bind(server_address)

  buff_size = SocketTCP.HEADER_SIZE + 16 

  while True: 
    segment_bytes, address = server_socket.udp_socket.recvfrom(buff_size)
    segment = SocketTCP.parse_segment(segment_bytes)
    print(segment["DATOS"].decode(), end="", flush=True)

