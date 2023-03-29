import socket
import pickle


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = socket.gethostname()
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p, self.game_id = self.connect()

    def get_p(self):
        return self.p

    def get_game_id(self):
        return self.game_id

    def connect(self):
        try:
            self.client.connect(self.addr)
            response = self.client.recv(4096).decode().split(',')
            return int(response[0]), response[1]
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(4096))
        except Exception as e:
            print(e)

# n = Network()
# print(n.send("hello"))
# print(n.send("working"))