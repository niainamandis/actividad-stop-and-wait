import socket

class SocketTCP:

  HEADER_SIZE = 7

  def __init__(self):
    self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    self.origin_address = None # se llena en bind
    self.dest_addres = None # se llena en connect/accept
    self.seq = None # se define en el handshake

  def bind(self, address):
    self.udp_socket.bind(address)
    self.origin_address = address      

  @staticmethod
  def parse_segment(segment_bytes): 
    return {
      "SYN": segment_bytes[0],
      "ACK": segment_bytes[1],
      "FIN": segment_bytes[2],
      "SEQ": int.from_bytes(segment_bytes[3:7], "big"),
      "DATOS": segment_bytes[7:],
    }

  @staticmethod
  def create_segment(segment): 
    header = bytes([segment["SYN"], segment["ACK"], segment["FIN"]])
    header += segment["SEQ"].to_bytes(4, "big")
    return header + segment["DATOS"]


