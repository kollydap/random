import pika

class Chatroom:
    def __init__(self, room_name: str) -> None:
        self.room_name = room_name

    def connect(self, user):
        print(f"{user.username} has joined room '{self.room_name}'.")

    def send_message(self, message: str):
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host="localhost")
        )
        channel = connection.channel()
        channel.basic_publish(exchange="", routing_key=self.room_name, body=message)

    def start_listening(self):
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host="localhost")
        )
        channel = connection.channel()
        channel.queue_declare(queue=self.room_name)
        channel.basic_consume(
            queue=self.room_name, on_message_callback=self.message_received, auto_ack=True
        )
        print(f"Started listening to room '{self.room_name}'...")
        channel.start_consuming()

    def message_received(self, ch, method, properties, body: str):
        print(f"\nMessage received in room '{self.room_name}': {body.decode('utf-8')}\n")
