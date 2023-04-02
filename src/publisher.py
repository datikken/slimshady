import pika

credentials = pika.PlainCredentials('user', 'password')
connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1', credentials=credentials))

channel = connection.channel()
channel.queue_declare(queue="hello")

channel.basic_publish(exchange="", routing_key="hello", body="hello_world 2")
print("[x] Sent Hello World")

connection.close()
