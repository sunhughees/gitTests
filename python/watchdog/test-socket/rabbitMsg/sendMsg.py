import pika

class SendRabbitMessage():

    def __init__(self, queue='default_task', host='localhost'):

        self.taskQueue = queue

        self.hostName = host

        self.__connection = pika.BlockingConnection(pika.ConnectionParameters(host))

        self.__channel = self.__connection.channel()

        self.__channel.queue_declare(queue=self.taskQueue, durable=True)

    def sendMessage(self, msg):

        self.__channel.basic_publish(exchange='',
                                     routing_key=self.taskQueue,
                                     body=msg)
        print 'sent: "' + msg + '"\n' 



    def __del__(self):

        self.__connection.close()
        print 'close rabbitServer\'s connection'


if __name__ == '__main__':

    sendOneMessage = SendRabbitMessage(queue='myTask-1')
    sendOneMessage.sendMessage(msg='Hello, World!')
    del sendOneMessage
