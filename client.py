import socket
from colorama import Fore, Style, init

def error(text):
    print(Fore.RED + text + Style.RESET_ALL)

def success(text):
    print(Fore.GREEN + text + Style.RESET_ALL)

def title(text):
    print(Fore.YELLOW + text + Style.RESET_ALL)


title("===TeChat===")
print("Напишите /exit чтобы выйти")

client = socket.socket() 
client.connect(("localhost", 12345)) # Подключаемся к серверу

while True:
    message = input("Введите сообщение: ")

    if message == "/exit":
        break

    client.send(message.encode()) # Переводим сообщение в двоичный код и отправляем

client.close()