import socket

client = socket.socket()
client.connect(("localhost", 12345))

want_send = True

while want_send == True:
    message = input("Введите сообщение: ")
    client.send(message.encode())