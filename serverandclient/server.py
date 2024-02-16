import socket
import threading


def handle_client(conn, addr):
    print(f"Connection from: {addr}")
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print(f"Received from {addr}: {data}")
        data = input("->")
        conn.send(data.encode())
    print(f"Client {addr} disconnected")
    conn.close()


def main():
    host = "127.0.0.1"
    port = 5001
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mySocket.bind((host, port))
    mySocket.listen(5)

    print("Server listening on port", port)

    while True:
        conn, addr = mySocket.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()


main()
