import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 5000))

ime = input("Unesi ime: ")

def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode()
            print(message)
        except:
            break

thread = threading.Thread(target=receive_messages)
thread.start()

while True:
    poruka = input()

    if poruka.lower() == "exit":
        break

    client.send(f"{ime}: {poruka}".encode())

client.close()