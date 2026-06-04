import socket

def ucitaj_redove(naziv_fajla):
    with open(naziv_fajla, "r") as file:
        return [red.strip() for red in file.readlines()]

server1_redovi = ucitaj_redove("server1_data.txt")
server2_redovi = ucitaj_redove("server2_data.txt")

HOST = "localhost"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

poruka = client.recv(1024).decode()
print("Poruka od Server2:", poruka)

redovi_za_slanje = []

for red in server1_redovi:
    if red not in server2_redovi:
        redovi_za_slanje.append(red)

print("Redovi koje Server1 treba da posalje Server2:")

for red in redovi_za_slanje:
    print(red)

client.close()