import socket
from _thread import *
import sys

# server = "162.247.88.151" # Lofts
server = "10.245.202.223" # UVM
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Server started. Waiting for a connection...")


def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


pos = [(0, 0), (100, 100)]


def threaded_client(conn, player):
    conn.send(str.encode(make_pos(pos[player])))
    reply = ""
    while True:
        try:
            data = read_pos(conn.recv(2048).decode())
            pos[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]

                # print("Received: ", data)
                # print("Sending: ", reply)

            conn.sendall(str.encode(make_pos(reply)))
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