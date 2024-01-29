import socket


def main():
    host = "127.0.0.1"
    port = 5000
    mySocket = socket.socket()
    mySocket.bind((host, port))
    mySocket.listen(1)

    conn, addr = mySocket.accept()
    print(f"connection from: {addr}")
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print(f"from {addr}: {str(data)}")
        data = str(data).upper()
        conn.send(data.encode())

    conn.close()


main()
