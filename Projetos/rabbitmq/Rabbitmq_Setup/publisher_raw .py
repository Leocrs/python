import pika

def minha_callback(ch, method, properties, body):
    print(body)

Connection_parameters = pika.connection.ConnectionParameters(
    host="localhost",
    port=5672,
    credentials=pika.PlainCredentials(
        username="guest",
        password="guest"
    )
)

channel = pika.BlockingConnection(Connection_parameters).channel()
channel.basic_publish(
    exchange="data_exchange",
    routing_key="",
    body="Teste de mensagem, vamos ver se funciona?".encode(),
    properties=pika.BasicProperties(
        delivery_mode = 2,
    )
 
)
