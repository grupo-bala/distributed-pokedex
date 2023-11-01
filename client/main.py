from network.client import Client

client = Client("127.0.0.1:9090")
client.send_message()