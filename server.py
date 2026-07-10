from storage import load_database, save_database
import socket
import threading

HOST = "127.0.0.1"
PORT = 5000

# Shared database
database = load_database()

# Lock for thread-safe access
lock = threading.Lock()


def handle_client(client_socket, client_address):
    print(f"[+] Client Connected: {client_address}")

    client_socket.send(
        "Welcome to Distributed Key Value Store!\n".encode()
    )

    while True:
        try:
            command = client_socket.recv(1024).decode().strip()

            if not command:
                break

            print(f"[{client_address}] {command}")

            parts = command.split()

            if len(parts) == 0:
                client_socket.send("Invalid Command".encode())
                continue

            operation = parts[0].upper()

            # ---------------- SET ----------------
            if operation == "SET":

                if len(parts) < 3:
                    client_socket.send(
                        "Usage: SET <key> <value>".encode()
                    )
                    continue

                key = parts[1]
                value = " ".join(parts[2:])

                with lock:
                    database[key] = value
                    save_database(database)

                client_socket.send("OK".encode())

            # ---------------- GET ----------------
            elif operation == "GET":

                if len(parts) < 2:
                    client_socket.send(
                        "Usage: GET <key>".encode()
                    )
                    continue

                key = parts[1]

                with lock:
                    value = database.get(key, "Key Not Found")

                client_socket.send(value.encode())

            # ---------------- DELETE ----------------
            elif operation == "DELETE":

                if len(parts) < 2:
                    client_socket.send(
                        "Usage: DELETE <key>".encode()
                    )
                    continue

                key = parts[1]

                with lock:
                    if key in database:
                        del database[key]
                        save_database(database)
                        client_socket.send("Deleted".encode())
                    else:
                        client_socket.send("Key Not Found".encode())

            # ---------------- KEYS ----------------
            elif operation == "KEYS":

                with lock:
                    keys = ", ".join(database.keys())

                if keys == "":
                    keys = "Database Empty"

                client_socket.send(keys.encode())

            # ---------------- COUNT ----------------
            elif operation == "COUNT":

                with lock:
                    count = str(len(database))

                client_socket.send(count.encode())

            # ---------------- EXIT ----------------
            elif operation == "EXIT":

                client_socket.send("Goodbye".encode())
                break

            # ---------------- INVALID ----------------
            else:
                client_socket.send(
                    "Invalid Command".encode()
                )

        except Exception as e:
            print("Error:", e)
            break

    client_socket.close()

    print(f"[-] Client Disconnected: {client_address}")


# Create Server Socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))

server.listen(5)

print("=" * 50)
print(" Distributed Key Value Store Server")
print("=" * 50)
print(f"Server started on {HOST}:{PORT}")
print("Waiting for clients...\n")


while True:
    client_socket, client_address = server.accept()

    thread = threading.Thread(
        target=handle_client,
        args=(client_socket, client_address)
    )

    thread.start()
