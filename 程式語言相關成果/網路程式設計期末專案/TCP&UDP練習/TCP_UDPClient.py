import socket


ip = socket.gethostbyname(socket.gethostname())
def send_tcp(message):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip,8888))

    data = ('TCP :' + message)
    s.send(data.encode())
    print(s.recv(1024).decode())
    s.close()

def send_udp(message):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = ('UDP :' + message)
    s.sendto(data.encode(), (ip,8889))
    dat, addr = s.recvfrom(8000)
    print(dat.decode())
    s.close()

if __name__ == '__main__':
    abc = input('輸入tcp or udp:')
    message = input('message :')
    if abc == 'tcp':
        send_tcp(message)
    else:
        send_udp(message)
