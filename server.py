import socket
from _thread import *
import pickle
from game import Game

server = socket.gethostname()
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Server started on address:", str(s.getsockname()[0]))
print("Waiting for a connection...")

connected = set()
games = {}
id_count = 0


def threaded_client(conn, p):
    global id_count

    reply = ""
    while True:
        try:
            data = conn.recv(4096).decode()

            if game_id in games:
                game = games[0]

                if not data:
                    break
                else:
                    if data == "games":
                        pass
                        # conn.sendall(pickle.dumps(games))
                    elif data != "get":
                        game.play(p, data)

                    reply = game
                    # conn.sendall(pickle.dumps(reply))

            else:
                break
        except:
            break

    print("Lost connection")

    try:
        del games[game_id]
        print("Closing game", game_id)
    except:
        pass

    id_count -= 1
    conn.close()


while True:
    conn, addr = s.accept()
    print("Connected to:", addr[0])

    id_count += 1
    game_id = (id_count - 1) // 4

    if id_count > 5:
        conn.send(str.encode("full"))
    else:
        if id_count == 1:
            games[game_id] = Game(game_id)
        conn.send(str.encode(str(id_count)))
        start_new_thread(threaded_client, (conn, id_count))
