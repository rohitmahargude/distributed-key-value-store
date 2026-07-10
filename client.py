import socket

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

welcome = client.recv(1024).decode()
print(welcome)

while True:

    command = input(">> ")

    client.send(command.encode())

    response = client.recv(1024).decode()

    print(response)

    if command.upper() == "EXIT":
        break

client.close()
