# Imports
import socket

#Variables
PORT = 5673
HEADER = 64
FORMAT = 'utf-8'
SERVER = "192.168.43.90"
ADDR = (SERVER, PORT)


class Net:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(ADDR) 
    

    def disconnect(self):
        self.send("DISCONNECT", "Socket")


    def send(self, msg, Type):
        message = str.encode("{}\n\n{}".format(Type, msg))
        self.client.send(message)


    def receive(self):
        print("received from the server")
        msg_header = self.client.recv(HEADER).decode(FORMAT)
        print(msg_header)
        print(str(msg_header.split("\n")[0]))
        msg_length = int(msg_header.split("\n")[0])
        return self.client.recv(msg_length).decode(FORMAT)
