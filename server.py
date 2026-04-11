import socket
from colorama import Fore, Style, init

def error(text):
    print(Fore.RED + text + Style.RESET_ALL)

def success(text):
    print(Fore.GREEN + text + Style.RESET_ALL)

def title(text):
    print(Fore.YELLOW + text + Style.RESET_ALL)

server = socket.socket()
server.bind(("localhost", 12345))
server.listen()

client, addr = server.accept()



while True:
    try:
        data = client.recv(1024).decode()

        if not data:
            error("Клиент отключился")
            break

        print("Получено:", data)

    except: 
        error("Клиент отключился")
        break

client.close()
server.close()