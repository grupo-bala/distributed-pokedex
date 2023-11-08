from util.singleton import SingletonMeta
import socket as sk

class Client(metaclass=SingletonMeta):
    def __init__(self, server_addr: str) -> None:
        self.socket = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
        self.socket.settimeout(2.0)

        (ip, port) = server_addr.split(":")
        self.server_addr = (ip, int(port))
    
    def send_message(self, msg: str):
        self.socket.sendto(msg.encode("utf-8"), self.server_addr)
            
    def receive_message(self) -> bytes:
        while True:
            data = self.socket.recv(1024)
            
            return data
        
client = Client("127.0.0.1:9090")