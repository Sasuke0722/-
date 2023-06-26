import socket
import threading
import os


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
            c, addr = self.s.accept()
            print('---連線成功---')
            print(c)

            threading.Thread(target=self.handle_c, args=(c, addr,)).start()    # 執行序多工

    def handle_c(self, c, addr):
        getFilename = c.recv(1024)    # 接收檔名並建檔
        getFilename = getFilename.decode()
        fp = open(getFilename, 'w')
        print('生成檔案 :'+ getFilename)
        getdata = c.recv(1024)    # 接收內容
        fp.write(getdata.decode())    # 寫入檔案
        print('上傳完成...')
        c.send('ok'.encode())
        fp.close()
        c.close()
        print('結束連線')



server = Server()