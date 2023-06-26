import socket
import threading
import time

list_of_client = [] # 以全域變數宣告一個串列

def broadcast(message, c, name): # 將接收到的 Client端 訊息進行廣播(大家都看的到)
    for client in list_of_client:
        if client != c:
            client.send((name+' :'+message).encode())

def remove(connection): # 將離開的使用者移出 list_of_client 串列
    if connection in list_of_client:
        list_of_client.remove(connection)

class Server:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.accept_connections()


    def accept_connections(self):
        ip = socket.gethostbyname(socket.gethostname())    # 取得本地端 IP
        port = int(input('Enter port --> '))    # 輸入 port


        self.s.bind((ip, port))
        self.s.listen(100)

        print('Running on IP: ' + ip)
        print('Running on port: ' + str(port))
        print('等待請求...')

        while 1:
            c, addr = self.s.accept() # 接受連線
            list_of_client.append(c)
            print(c)
            print('---連線成功---')

            threading.Thread(target=self.handle_c, args=(c, addr,)).start()    # 執行序多工

    def handle_c(self, c, addr):
        userName = c.recv(1024).decode()
        c.send(('Welcome '+userName).encode())

        while True:
            message = c.recv(1024).decode()

            if message != 'exit':
                print(userName + ':' + message)
                message_to_send = message
                broadcast(message_to_send, c, userName)
            else:
                list_of_client.remove(c)
                c.send('You exit'.encode())
                print(userName,' exit.')
                broadcast((userName+' is Loging out...'), c,userName)
                time.sleep(1)
                c.close()
                break
            if message == 'exit':
                break







server = Server()