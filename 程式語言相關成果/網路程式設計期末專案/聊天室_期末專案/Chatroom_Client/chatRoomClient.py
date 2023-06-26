import socket
import threading
import time
import os

class Client:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # "socket.SOCK_STREAM"是 Socket Type 的一個常數，用於指定 TCP 連接
        self.connect_to_server() # 連線請求

    def connect_to_server(self): # 通過 Port 連線到對應 Server 端
        self.ip = socket.gethostbyname(socket.gethostname())
        self.port = input('Enter port --> ') 

        self.s.connect((self.ip, int(self.port)))

        self.main()

    def reconnect(self): # 如果連接中斷，這個方法可以重新連接到伺服器。
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.ip, int(self.port)))


    def main(self):
        self.name = input('Enter your name :')
        self.s.send(self.name.encode()) 
        print(self.s.recv(1024).decode())
        while True:
            msg = input()  # 使用者輸入訊息
            self.s.send(msg.encode())
            r = threading.Thread(target=self.recv_msg, args=())
            w = threading.Thread(target=self.write_msg, args=(self.name,))
            r.start()
            w.start()
            r.join()
            w.join()
            break

    def recv_msg(self): # 持續接收訊息，以2048字元為上限
        while True:
            message = self.s.recv(2048) # 接收訊息，以2048字元為上限
            print(message.decode())
            if message.decode == 'You exit': 
                break

    def write_msg(self, name):
        while True:
            message = input(name+":")
            self.s.send(message.encode())
            if message == 'exit':
                break


client = Client()