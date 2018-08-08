import socket

HOST = ""
PORT = 10000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind((HOST, PORT))

while 1:
    print (s.recv(50))