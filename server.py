import socket

server = socket.socket()
server.bind(("localhost", 12345))
server.listen()

client, addr = server.accept()

server_open = True

while server_open == True:
    data = client.recv(1024).decode()
    print("Получено:", data)