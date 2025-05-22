import socket

HOST = 'localhost'
PORT = 5000

def start_server(address: str, port: int):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((address, port))
    server_socket.listen(1)
    print(f"Servidor TCP rodando em {address}:{port}...")

    while True:
        client, addr = server_socket.accept()
        print(f'Conexão aceita de {addr}')
        data = client.recv(1024)
        if not data:
            break
        print(f'Mensagem recebida: {data.decode()}')
        client.sendall('Mensagem recebida!'.encode())
        client.close()

if __name__ == "__main__":
    start_server(HOST, PORT)