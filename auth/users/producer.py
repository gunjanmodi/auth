
import pika, json

params = pika.URLParameters('amqps://xxbyfftl:ST-i9QFY1y-3C-LAS9wJwOaLt5SoEWmW@snake.rmq2.cloudamqp.com/xxbyfftl')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
