import pika

def minha_callback(ch, method, properties, body):
    print(body)

Connection_parameters = pika.connection.ConnectionParameters(
    host="localhost", port=5672,
    credentials=pika.PlainCredentials(
        username="guest",
        password="guest"
    )
)

channel = pika.BlockingConnection(Connection_parameters).channel()
channel.queue_declare(
    queue="data_queue", 
    durable=True
    
)

channel.basic_consume(
    queue="data_queue",
    auto_ack=True,
    on_message_callback=minha_callback
)

print(f"Listen RabbitMQ on port 5672")
channel.start_consuming()