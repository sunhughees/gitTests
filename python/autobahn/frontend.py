from os import environ
from twisted.internet.defer import inlineCallbacks
from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner
# or: from autobahn.asyncio.wamp import ApplicationSession


class MyComponent(ApplicationSession):

    @inlineCallbacks
    def onJoin(self, details):

        print("session ready")

        # listening for the corresponding message from the "backend"
        # (any session that .publish()es to this topic).
        # def onevent(msg):
        #     print("Got event: {}".format(msg))

        # yield self.subscribe(onevent, u'com.myapp.hello')

        # self.publish('com.myapp.hello', 'Hello, world!')

        # def add2(x, y):
        #     return x+y

        # self.register(add2, 'com.myqpp.add2')

        # # call a remote procedure.
        # res = yield self.call(u'com.myapp.add2', 2, 3)
        # print("Got result: {}".format(res))


if __name__ == '__main__':

    # runner = ApplicationRunner(
    #     environ.get("AUTOBAHN_DEMO_ROUTER", u"ws://127.0.0.1:8080/ws"),
    #     u"crossbardemo",
    # )

    runner = ApplicationRunner(url=u"ws://localhost:9000/ws", realm=u"realm1")
    runner.run(MyComponent)
