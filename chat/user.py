import pika

class User:
    def __init__(self, username: str, room_name: str) -> None:
        self.username = username
        self.room_name = room_name

    def listen(self):
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host="localhost")
        )
        channel = connection.channel()
        channel.queue_declare(queue=self.room_name)
        channel.basic_consume(
            queue=self.room_name, on_message_callback=self.message_listener, auto_ack=True
        )
        print(f"{self.username} is now listening to messages in room '{self.room_name}'...")
        channel.start_consuming()

    def message_listener(self, ch, method, properties, body: str):
        print(f"\n{self.username} received: {body.decode('utf-8')}\n")
        self.listen()  # Listen for more messages after receiving one

    def send_message(self, message: str):
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host="localhost")
        )
        channel = connection.channel()
        channel.basic_publish(exchange="", routing_key=self.room_name, body=message)
        print(f"{self.username} sent: {message}\n")
