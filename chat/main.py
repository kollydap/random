from user import User
from chatroom import Chatroom
import threading

def main():
    room_name = "happy_boys"
    chatroom = Chatroom(room_name=room_name)

    kolawole = User(username="kolawole", room_name=room_name)
    dupe = User(username="dupe", room_name=room_name)

    chatroom.connect(kolawole)
    chatroom.connect(dupe)

    listener_thread = threading.Thread(target=chatroom.start_listening)
    listener_thread.start()

    kolawole.send_message("Hello from Kolawole!")
    dupe.send_message("Hi, Dupe here!")

    kolawole.listen()
    dupe.listen()

if __name__ == "__main__":
    main()
