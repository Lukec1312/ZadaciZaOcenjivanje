import socket

HOST = "localhost"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("Server2 ceka vezu...")

conn, addr = server.accept()
print("Server1 se povezao.")
print("Server2 je spreman za replikaciju.")

conn.send("Server2 spreman".encode())

conn.close()
server.close()