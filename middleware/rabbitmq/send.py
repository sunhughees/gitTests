# -*- coding: utf-8 -*-
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.queue_declare(queue='my_task', durable=True) # durable

if len(sys.argv) < 2:
    print 'message is empty'
    sys.exit(0)

message = str(sys.argv[1])

channel.basic_publish(exchange='',
                      routing_key='my_task',
                      body=message,
                      # make message persistent
                    #   properties=pika.BasicProperties(delivery_mode=2)
                      )

print 'sent:"'+message+'"\n'

connection.close()
