#!/usr/bin/python
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("10.12.27.235", 1111))
print("Connection Established To Server")
while True:
    message = sock.recv(1024).decode()
    print(message)
    if message == "q":
        break
    else:
        message_back = input("Type Message To Send To Server: ")
        sock.send(message_back.encode())
sock.close()
