import asyncio
import time


@asyncio.coroutine
def sleepy():
    print("Befoer sleep", time.time())
    yield from asyncio.sleep(5)
    print("After sleep", time.time())


asyncio.get_event_loop().run_until_complete(sleepy())
print("Stating async io process")

loop = asyncio.get_event_loop()

command = ''


class EchoProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport
        print(transport)

    def data_received(self, data):
        print(data, type(data))
        self.transport.write(data)

    def connection_lost(self, exc):
        server.close()


server = loop.run_until_complete(
    loop.create_server(EchoProtocol, '127.0.0.1', 4444))

server = loop.run_until_complete(
    loop.create_server(EchoProtocol, '127.0.0.1', 4445))    
loop.run_until_complete(server.wait_closed())
