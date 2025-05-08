import socket
import threading

def receive_messages(sock):
    while True:
        try:
            data, _ = sock.recvfrom(1024)
            print(f"\n[OUTRO CLIENTE] {data.decode()}\nDigite sua mensagem: ", end="")
        except:
            break

def start_client(address: str, port: int):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Thread para receber mensagens
    threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()

    while True:
        message = input('Digite sua mensagem: ')
        client_socket.sendto(message.encode(), (address, port))

if __name__ == "__main__":
    start_client('localhost', 6000)