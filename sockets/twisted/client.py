from twisted.internet import reactor, protocol

class ChatClient(protocol.Protocol):
    def connectionMade(self):
        self.transport.write("Hola servidor, soy el cliente.".encode())

    def dataReceived(self, data):
        print("Servidor dice:", data.decode())

    def sendMessage(self, message):
        self.transport.write(message.encode())

class ChatClientFactory(protocol.ClientFactory):
    def buildProtocol(self, addr):
        return ChatClient()

    def clientConnectionFailed(self, connector, reason):
        print("Conexión fallida.")
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print("Conexión perdida.")
        reactor.stop()

reactor.connectTCP("localhost", 8123, ChatClientFactory())
reactor.run()