import socket
import pickle


class Network:
    def __init__(self, ip):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = ip
        self.port = 5555
        self.addr = (self.server, self.port)
        self.game = self.connect()

    def get_game(self):
        return self.game

    def connect(self):
        try:
            # print("Attempting connection on " + self.server)
            self.client.connect(self.addr)
            response = pickle.loads(self.client.recv(4096))
            return response
        except:
            print("Error Connecting to server...")
            return None

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(4096))
        except Exception as e:
            print(e)

# n = Network()
# print(n.send("hello"))
# print(n.send("working"))