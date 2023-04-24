import socket
from _thread import *
import pickle
from game import Game

server = 'localhost'
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print('Server started on address:', str(s.getsockname()[0]))
print('Waiting for a connection...')

connected = set()
games = {}
id_count = 0


def threaded_client(conn, p, game_id):
    global id_count

    while True:
        try:
            data = conn.recv(4096).decode()

            if game_id in games:
                game = games[game_id]



                if not data:
                    break
                else:
                    if data == 'start':
                        if p == 1 and game.get_num_players() >= 2:
                            game.set_screen('TURNS')
                    elif data[:4] == 'icon':
                        game.set_icon(p - 1, int(data[4]))
                    elif data == 'roll':
                        game.roll()
                    elif data == 'done roll':
                        game.done_roll(game.dice_values[0] + game.dice_values[1])
                        game.next_player()

                    conn.sendall(pickle.dumps(game))
            else:
                break
        except:
            break

    print('Lost connection')

    try:
        del games[game_id]
        print('Closing game', game_id)
    except:
        pass

    id_count -= 1
    conn.close()


while True:
    conn, addr = s.accept()
    print('Connected to:', addr[0])

    id_count += 1
    game_id = (id_count - 1) // 4

    if id_count > 5:
        conn.send(str.encode('-1'))
    elif game_id in games and games[game_id].current_screen != 1:
        conn.send(str.encode('-2'))
    else:
        if id_count == 1:
            games[game_id] = Game(game_id)
        games[game_id].add_player()
        conn.send(str.encode(str(id_count)))
        start_new_thread(threaded_client, (conn, id_count, game_id))
