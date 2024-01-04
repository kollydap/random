import pika
import requests


def consume_messages():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    channel = connection.channel()

    channel.queue_declare(queue="image_processor")
    channel.basic_consume(
        queue="image_processor", on_message_callback=auth_listener, auto_ack=True
    )

    print(" [*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()


def auth_listener(ch, method, properties, body: str):
    endpoint = 'http://localhost:5229'
    image_url = f"{endpoint}{body.decode('utf-8').split('wwwroot')[1]}"
    print(image_url)
    output_file = 'image.jpg'
    download_image(image_url, output_file)
    

def download_image(url, destination_file):
    response = requests.get(url)

    if response.status_code == 200:
        with open(destination_file, 'wb') as file:
            file.write(response.content)
        print(f"Image downloaded and saved as {destination_file}")
    else:
        print(f"Failed to download image. Status code: {response.status_code}")

consume_messages()
