from select import select
import socket

host = socket.gethostbyname(socket.gethostname())
def read_tcp(s):
    while True:
        client,addr = s.accept()
        data = client.recv(8000)
        client.send(data)
        data.decode()
        print("Recv TCP:'%s'" % data)
        client.close()
        break

def read_udp(s):
    while True:
        data,addr = s.recvfrom(8000)
        data = data.decode()
        s.sendto(data.encode(), addr)
        print("Recv UDP:'%s'" % data)
        break

def run():
    port = 8888
    size = 8000
    backlog = 5

    # create tcp socket
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.bind((host,port))
    tcp.listen(backlog)

    # create udp socket
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp.bind((host,8889))

    input = [tcp,udp]

    while True:
        inputready,outputready,exceptready = select(input,[],[])

        for s in inputready:
            if s == tcp:
                read_tcp(s)
            elif s == udp:
                read_udp(s)
            else:
                print("unknown socket:", s)

if __name__ == '__main__':
    run()