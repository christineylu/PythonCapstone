import socket, pickle
'''Attempted to make this usable from any local server but kept getting an error'''
# from multiprocessing.connection import Client
# client = Client(('localhost', 1234))

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        '''Running on local server'''
        self.server = "0.0.0.0"
        # self.server = "127.0.0.1"
        # self.server = "192.168.1.17"
        # self.server = "192.168.1.17"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()
        print(self.p)

    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)

n = Network()
print (n.addr)