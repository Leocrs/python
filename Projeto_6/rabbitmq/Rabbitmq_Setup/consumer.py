import pika
class RabbitMQConsumer:
    def __init__(self,callback) -> None:
        self.__host = "localhost"
        self.__port = 5672
        self.__username = "guest"
        self.__password = "guest"
        self.__queue_name = "data_queue"
        self.__callback = callback
        self.__channel = self.create_channel()

    def __create_channel(self):
        Connection_parameters = pika.connection.ConnectionParameters(
            host="localhost",
            port=5672,
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
            on_message_callback=self.minha_callback
        )
        
        return channel
    
    def start(self):
        print("Listen RabbitMQ on port 5672")
        self.__channel.start_consuming()
        
        
def callback(ch, method, properties, body):
    print(body)
    
RabbitMQConsumer=RabbitMQConsumer(callback)
RabbitMQConsumer.start()
        