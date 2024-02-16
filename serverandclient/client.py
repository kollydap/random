import socket


def main():
    host = "127.0.0.1"
    port = 5001
    mySocket = socket.socket()
    mySocket.connect((host, port))

    message = input("->")
    while message != "q":
        mySocket.send(message.encode())
        data = mySocket.recv(1024).decode()
        print(f"Received from server: {data}")
        message = input("->")
    mySocket.close()


main()
