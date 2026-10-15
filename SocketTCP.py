import socket
import random

class SocketTCP:

  HEADER_SIZE = 7

  def __init__(self):
    self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    self.origin_address = None # se llena en bind
    self.dest_address = None # se llena en connect/accept
    self.seq = None # se define en el handshake

  def bind(self, address):
    self.udp_socket.bind(address)
    self.origin_address = address      

  def connect(self, address):
    buff_size = self.HEADER_SIZE + 16
    self.dest_address = address
    # numero random entre 0 y 100 para handshake
    self.seq = random.randint(0,100)
    seg = {
        "SYN": 1, "ACK": 0, "FIN": 0,
        "SEQ": self.seq, "DATOS": b""
        }
    self.udp_socket.sendto(self.create_segment(seg), self.dest_address)

    # esperamos respuesta
    seg_bytes, resp_address = self.udp_socket.recvfrom(buff_size)
    resp = self.parse_segment(seg_bytes)
    if (resp["SYN"] == 1 and resp["ACK"] == 1):
      self.dest_address = resp_address
      self.seq += 1
      seg_2 = {
          "SYN": 0, "ACK": 1, "FIN": 0,
          "SEQ": self.seq, "DATOS": b""
          }
      self.udp_socket.sendto(self.create_segment(seg_2), self.dest_address)

  def accept(self):
    buff_size = self.HEADER_SIZE + 16
    # esperando
    while True:
      seg_bytes, client_address = self.udp_socket.recvfrom(buff_size)
      seg = self.parse_segment(seg_bytes)
      if (seg["SYN"] == 1 and seg["ACK"] == 0):
        break

    new_sock = SocketTCP()
    new_sock.bind((self.origin_address[0], 0))
    new_sock.origin_address = new_sock.udp_socket.getsockname()
    new_sock.dest_address = client_addresr
    new_sock.seq = random.randint(0, 100)
    seg_resp = {
        "SYN": 1, "ACK": 1, "FIN": 0,
        "SEQ": new_sock.seq, "DATOS": b""
        }
    new_sock.udp_socket.sendto(new_sock.create_segment(seg_resp), client_address)

    # esperar el ACK = 1
    while True:
      seg_bytes, addr = new_sock.udp_socket.recvfrom(buff_size)
      seg_2 = self.parse_segment(seg_bytes)
      if (seg_2["ACK"] == 1 and addr == client_address):
        new_sock.seq += 1
        break

    return new_sock, new_sock.origin_address


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


