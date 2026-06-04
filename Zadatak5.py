def server():
    return "Podaci sa servera: korisnicki profil, fajlovi, dokumenti"


def interceptor(token):
    validan_token = "12345"

    if token != validan_token:
        return "Pristup odbijen"
    else:
        return server()


token = input("Unesi token: ")

odgovor = interceptor(token)

print(odgovor)