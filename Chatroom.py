import pika
import threading


class Chatroom:
    def __init__(self, user_name: str, room_name: str) -> None:
        # a list of connected 
        self.user_name = user_name
        self.room_name = room_name
        listening_thread = threading.Thread(target=self.open_channel, args=(self.room_name,))
        listening_thread.start()
        # creTE a thread that fetches from the database


    def disconnect():
        ...
    
    
    def open_channel(self, room_name):
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host="localhost")
        )
        channel = connection.channel()

        channel.queue_declare(queue=room_name)
        channel.basic_consume(
            queue=room_name, on_message_callback=self.message_listener, auto_ack=True
        )

        print(" [*] Waiting for messages. To exit press CTRL+C")
        channel.start_consuming()

    def message_listener(ch, method, properties, body: str):
        print(body.decode("utf-8"))


chat1 = Chatroom(user_name="kolawole", room_name="happy")
chat2 = Chatroom(user_name="Jennifer", room_name="happy")
chat3 = Chatroom(user_name="Nobody", room_name="happy")
