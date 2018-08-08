import socket
import time
import datetime

HOST = "10.108.139.206"
PORT = 10000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while 1:
    data = datetime.datetime.now()
    s.sendto(data, (HOST, PORT))
    print ("sent" + data)
    time.sleep(0.1)