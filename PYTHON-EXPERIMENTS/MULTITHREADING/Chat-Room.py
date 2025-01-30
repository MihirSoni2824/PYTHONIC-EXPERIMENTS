import threading
import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 12345        # Port to listen on (non-privileged ports are 1024-65535)

def handle_client(conn, addr):
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print('Received message:', data.decode())
        for client in clients:
            if client!= conn:
                client.sendall(data)
    conn.close()
    clients.remove(conn)
    print('Client disconnected')

if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print('Server listening on port', PORT)

    clients = []
    while True:
        conn, addr = server_socket.accept()
        clients.append(conn)
        threading.Thread(target=handle_client, args=(conn, addr)).start()