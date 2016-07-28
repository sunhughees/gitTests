# -*- coding: utf-8 -*-
import pika
import sys

if len(sys.argv) < 2:
    print 'Message queue\'s name is empty!'
    sys.exit(0)

msgQueueName = str(sys.argv[1])

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.queue_declare(queue=msgQueueName, durable=True) # durable

print 'Waiting for messages. To exit press CRTL+C'

# callback function for channel.basic_consume
def callback(ch, method, properties, body):
    print ch
    print method
    print properties
    print body

channel.basic_consume(callback, queue=msgQueueName, no_ack=True)

channel.start_consuming()
