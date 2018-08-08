import socket
import time

HOST = "131.94.132.158"
PORT = 10000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while 1:
    timestamp = time.asctime()
    s.sendto(timestamp.encode('utf-8'), (HOST, PORT))
    print ("sent" + timestamp)
    time.sleep(0.1)