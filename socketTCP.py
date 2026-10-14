import socket

class SocketTCP:

  def __init__(self):
    self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    self.origin_address = None # se llena en bind
    self.dest_addres = None # se llena en connect/accept
    self.seq = None # se define en el handshake

