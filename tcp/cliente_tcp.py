import socket

def start_server(addrr: str, port: int):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((addrr, port))

    while True:
        message = input('digite a mensagem')
        server.sendto(menssage.encode(),)

        if_name_=='_main_':
        HOST='localhost'
        PORT=8000
        send_message_to_server(HOST, PORT)
   