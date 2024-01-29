from user import User
from chatroom import Chatroom
import threading

def main():
    room_name = "happy_boys"
    chatroom = Chatroom(room_name=room_name)

    username = input("Enter your username: ")
    user = User(username=username, room_name=room_name)

    chatroom.connect(user)

    listener_thread = threading.Thread(target=chatroom.start_listening)
    listener_thread.start()

    while True:
        message = input("Type your message (press Enter to send): ")
        user.send_message(message)

if __name__ == "__main__":
    main()
