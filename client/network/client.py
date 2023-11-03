import socket as sk

class Client:
    def __init__(self, server_addr: str) -> None:
        self.socket = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
        (ip, port) = server_addr.split(":")
        self.server_addr = (ip, int(port))
    
    def send_message(self, msg: str):
        self.socket.sendto(msg.encode("utf-8"), self.server_addr)