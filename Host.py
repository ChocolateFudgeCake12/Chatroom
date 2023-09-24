import socket
import multiprocessing
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

def main():
    username = input("What is your username? ") + ": "
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while True:
            clientconn, clientadd = s.accept()
            with clientconn:
                print(f"Connected by {clientadd}")
                while True: 
                    datatosend = username + input(username)
                    clientconn.sendall(datatosend.encode())
                    data = clientconn.recv(1024)
                    print(data.decode())

main()