import socket

def start_server(addr: str, port: int):
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    server_socket.bind((addr, port))
    clientes = set() #armazena os clientes conectados

    print(f"UDP server listening on {addr}:{port}")

    while True:
        data, address= server_socket.recvfrom(1024)
        clientes.add(address) #adiciona novo cliente
        print(f'{address[1]}-Message: {data}')
        
        # Envia para todos os clientes EXCETO o remetente
        for client in clientes:
            if client != address:
                server_socket.sendto(
                    f"Cliente {address[1]} disse: {data.decode()}".encode(),
                    client
                )


if __name__=="__main__":
    HOST= 'localhost'
    PORT= 6000
    start_server(HOST,PORT)