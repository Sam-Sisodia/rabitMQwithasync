import pika,sys , os
import logging
import json
import time
import uuid
import asyncio
class PikaClient:
    def __init__(self, process_callable,queue='taskqueue'):
       
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        self.queue = queue
        self.channel.queue_declare(queue=self.queue)
        self.callback_queue = 'taskqueue'   #--
        self.process_callable = process_callable
        print('Pika  Stat Pika -----   connection initialized----')

       



    # def publish(self,payload= {}):
    #     self.channel.basic_publish(exchange='', routing_key="taskqueue" , body=str(payload))
    #     print("punblished---")
    #     self.connection

  

    async def consume(self, loop):
        """Setup message listener with the current running loop"""
        connection =   self.connection
        channel =  connection.channel()
        channel.queue_declare(queue='taskqueue')
        channel.basic_consume(queue='taskqueue', on_message_callback=self.process_incoming_message ,auto_ack=True)
        print('Strating Consumer ---- : Established pika async listener (consumer)')
        return connection



    

    
    async def process_incoming_message(self, message):
        pass
        print(message)
    
        """Processing incoming message from RabbitMQ"""
        message.ack()
        body = message.body
        print(f'Received message  This is msg Body -- : {body}')
        if body:
            print("thi----------------------")
            self.process_callable(json.loads(body))

   


    def send_message(self, message: dict):
        """Method to publish message to RabbitMQ"""
        self.channel.basic_publish(exchange='',routing_key='taskqueue',
                                properties=pika.BasicProperties(reply_to='taskqueue',
                                correlation_id=str(uuid.uuid4()) ),
            body=json.dumps(message)
        

        )

        print(self.channel.basic_publish)

     


    




'''

credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters('rabbit-server1',
                                       5672,
                                       '/',
                                       credentials)

'''

