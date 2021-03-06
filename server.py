import socket
from _thread import *
import pickle
from game import Game
'''Attempted to make this usable from any server but kept getting an error'''
# from multiprocessing.connection import Listener
# server_sock = Listener(('localhost', port))
# conn = server_sock.accept()
# unpickled_data = conn.recv()
# server = "127.0.0.1"
# server = "192.168.1.17"
server = "0.0.0.0"
# port = 5555
# Local Server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# server = ''
port = 5555
server_ip = socket.gethostbyname(server)



# try:
#     s.bind((server, port))
# except socket.error as e:
#     str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

connected = set()
games = {}
idCount = 0


def threaded_client(conn, p, gameId):
    global idCount
    conn.send(str.encode(str(p)))

    reply = ""
    while True:
        try:
            data = conn.recv(2048).decode()
            reply = data.decode("utf-8")

            if not data:
                print ("disconnected")
                break

            if gameId in games:
                game = games[gameId]

                if not data:
                    print("disconnected")
                    break
                else:
                    if data == "reset":
                        game.resetWent()
                    elif data != "get":
                        game.play(p, data)

                    conn.send(pickle.dumps(game))
            else:
                break
        except:
            break

    print("Lost connection")
    try:
        del games[gameId]
        print("Closing Game", gameId)
    except:
        pass
    idCount -= 1
    conn.close()



while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    idCount += 1
    p = 0
    gameId = (idCount - 1)//2
    if idCount % 2 == 1:
        games[gameId] = Game(gameId)
        print("Creating a new game...")
    else:
        games[gameId].ready = True
        p = 1


    start_new_thread(threaded_client, (conn, p, gameId))