import socket

def client():
    host = 'localhost'
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        print("Conectado al servidor. Escriba 'salir' para terminar.")
        
        while True:
            msg = input("Enviar: ")
            if msg:  # Verifica que el mensaje no esté vacío
                client_socket.sendall(msg.encode('utf-8'))
                if msg.lower() == 'salir':
                    break
                data = client_socket.recv(1024)
                print('Recibido:', data.decode('utf-8'))

if __name__ == '__main__':
    client()