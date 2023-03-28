import socket
from _thread import *
import sys
from player import Player
import pickle

# server = "162.247.88.151" # Lofts
# server = "10.245.202.223" # UVM
server = ""
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Server started. Waiting for a connection...")

players = [Player(0, 0, 50, 50, (0, 255, 0)), Player(100, 100, 50, 50, (0, 255, 0))]


def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]

                # print("Received: ", data)
                # print("Sending: ", reply)

            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
    conn.close()
    return player - 1


current_player = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    print("Current player:", current_player)
    start_new_thread(threaded_client, (conn, current_player))
    current_player += 1