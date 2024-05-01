from twisted.internet import reactor, protocol

class Chat(protocol.Protocol):
    def connectionMade(self):
        if self.factory.clients is None:
            self.factory.clients = []  # Asegurarse de que clients está inicializado
        self.factory.clients.append(self)
        print(f"Cliente conectado desde {self.transport.getPeer()}")

    def connectionLost(self, reason):
        if self in self.factory.clients:
            self.factory.clients.remove(self)
        print(f"Cliente desconectado de {self.transport.getPeer()}")

    def dataReceived(self, data):
        message = data.decode()
        print(f"Mensaje de {self.transport.getPeer()}: {message}")
        if self.factory.clients:  # Verifica si hay clientes antes de iterar
            for client in self.factory.clients:
                if client != self:
                    client.transport.write(data)

class ChatFactory(protocol.Factory):
    def __init__(self):
        self.clients = []  # Inicialización explícita de clients

    def buildProtocol(self, addr):
        return Chat()

reactor.listenTCP(8123, ChatFactory())
print("Servidor de chat iniciado en el puerto 8123.")
reactor.run()
