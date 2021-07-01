
import pika, json

params = pika.URLParameters('amqps://xxbyfftl:ST-i9QFY1y-3C-LAS9wJwOaLt5SoEWmW@snake.rmq2.cloudamqp.com/xxbyfftl')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties,body):
    print('Received in admin')
    print(body)

channel.basic_consume(queue='admin', on_message_callback=callback)

print('started consuming')

channel.start_consuming()

channel.close()