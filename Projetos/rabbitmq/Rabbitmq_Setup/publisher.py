import pika

class RabbitMQPublisher:
  def __init__(self,callback) -> None:
        self.__host = "localhost"
        self.__port = 5672
        self.__username = "guest"
        self.__password = "guest"
        self.__channel = self.create_channel()
        
def create_channel(self):
    Connection_parameters = pika.connection.ConnectionParameters(
        host=self.__host,
        port=self.__port,
        credentials=pika.PlainCredentials(
            username=self.__username,
            password=self.__password
        )
    )
    channel = pika.BlockingConnection(Connection_parameters).channel()
    return channel