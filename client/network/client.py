import socket as sk
import jsonpickle
from network.message import Message

class Client:
    def __init__(self, server_addr: str) -> None:
        self.socket = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
        (ip, port) = server_addr.split(":")
        self.server_addr = (ip, int(port))
    
    def send_message(self):
        msg = Message(0, 90, "Calculadora", "somar", "{ a: 2, b: 4 }")
        msg: str = jsonpickle.encode(msg, unpicklable=False)

        self.socket.sendto(msg.encode("utf-8"), self.server_addr)