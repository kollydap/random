import pika


def open_channel(room_name, message):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    channel = connection.channel()

    channel.queue_declare(queue=room_name)
    channel.basic_publish(exchange="", routing_key=room_name, body=message)
    connection.close()
    # channel.basic_consume(
    #     queue=room_name, on_message_callback=self.message_listener, auto_ack=True
    # )

    print(" [*] Waiting for messages. To exit press CTRL+C")


open_channel(room_name="hello", message="helloboy")
open_channel(room_name="hello", message="helloboy")
open_channel(room_name="hello", message="helloboy")
open_channel(room_name="hello", message="helloboy")
open_channel(room_name="hello", message="helloboy")
