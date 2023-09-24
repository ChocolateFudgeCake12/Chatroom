import socket

HOST = "127.0.0.1"
PORT = 65432 

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);


clientSocket.connect((HOST,PORT))
username = input("What is your username? ") + ": "
while True:
        data = username + input(username)
        clientSocket.sendall(data.encode())
        data = clientSocket.recv(1024)
        print(data.decode())