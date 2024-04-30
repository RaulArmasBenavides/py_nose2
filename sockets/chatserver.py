import socket
import threading

def handle_client(conn, addr):
    print(f"Nueva conexión de {addr}")
    try:
        while True:
            msg = conn.recv(1024)
            if not msg:
                break
            msg = msg.decode('utf-8')
            print(f"Mensaje de {addr}: {msg}")
            conn.sendall(f"Echo: {msg}".encode('utf-8'))
    finally:
        conn.close()

def server():
    host = 'localhost'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()
    print(f"Servidor escuchando en {host}:{port}")

    try:
        while True:
            conn, addr = server_socket.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()
    finally:
        server_socket.close()

if __name__ == '__main__':
    server()