from typing import Dict
import pika
import json

class RabbitMQPublisher:
  def __init__(self,callback) -> None:
        self.__host = "localhost"
        self.__port = 5672
        self.__username = "guest"
        self.__password = "guest"
        self.__exchange = "data_exchange"
        self.__routing_key = "" 
        self.__channel = self.create_channel()
        self.__callback = callback
        
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

def send_message(self,body,dictionary:Dict):
    self.__channel.basic_publish(
        exchange=self.__exchange,
        routing_key=self.__routing_key,
        body=json.dumps(body),
        properties=pika.BasicProperties(
            delivery_mode = 2,
        )
    )
    
RabbitMQ_Publisher = RabbitMQPublisher(send_message)
RabbitMQ_Publisher.send_message({"Olá mundo"})

  
  
 

