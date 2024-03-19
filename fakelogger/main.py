from fakelogger import FakeLogger
import logging
class MyApplication:
    def __init__(self):
        # Crear una instancia de FakeLogger
        self.logger = FakeLogger()
        
        # Opcional: Configurar el nivel de log
        self.logger.setLevel(logging.DEBUG)  # Ajustar según sea necesario

    def do_something(self):
        # Usar el FakeLogger para diferentes niveles de logging
        self.logger.debug("Esto es un mensaje de debug")
        self.logger.info("Esto es un mensaje informativo")
        self.logger.warning("Esto es un mensaje de advertencia")
        self.logger.error("Esto es un mensaje de error")
        self.logger.critical("Esto es un mensaje crítico")

# Crear una instancia de MyApplication
app = MyApplication()

# Llamar a un método que usa el FakeLogger
app.do_something()