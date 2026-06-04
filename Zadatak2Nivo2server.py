import socket
import threading

clients = []

def handle_client(client):
    while True:
        try:
            message = client.recv(1024).decode()

            if not message:
                break

            print("Poruka:", message)

            for c in clients:
                if c != client:
                    c.send(message.encode())

        except:
            break

    clients.remove(client)
    client.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 5000))
server.listen()

print("Chat server je pokrenut...")

while True:
    client, address = server.accept()
    clients.append(client)

    print("Novi klijent povezan:", address)

    thread = threading.Thread(target=handle_client, args=(client,))
    thread.start()