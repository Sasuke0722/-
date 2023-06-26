import socket
import os


class Client:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect_to_server()

    def connect_to_server(self):
        self.ip = socket.gethostbyname(socket.gethostname())
        self.port = input('Enter port --> ')

        self.s.connect((self.ip, int(self.port)))

        self.main()

    def reconnect(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.ip, int(self.port)))

    def main(self):
        filename = input('Enter your file name :')
        fp = open(filename, 'r')
        self.s.send(filename.encode())    # 檔名送到 server端 進行建檔

        while True:
            data = fp.read(1024)
            if not data:
                print('end of file.')
                break
            print(data)
            self.s.send(data.encode())
            result = self.s.recv(1024)
            result = result.decode()
            if result == 'ok':
                self.s.close()
                print('結束連線')
                break


client = Client()