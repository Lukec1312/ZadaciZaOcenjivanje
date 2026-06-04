fajl_sistem = {
    "server1": {
        "data": {
            "folder": {
                "file.txt": "Sadrzaj fajla file.txt"
            }
        }
    },
    "server2": {
        "data": {
            "docs": {
                "test.txt": "Sadrzaj fajla test.txt"
            }
        }
    }
}


def server(naziv_servera, putanja):
    return f"Zahtev je prosledjen serveru {naziv_servera}. Fajl je pronadjen: {putanja}"


def middleware(putanja):
    delovi = putanja.strip("/").split("/")

    trenutni_nivo = fajl_sistem
    najbliza_putanja = ""

    for deo in delovi:
        if deo in trenutni_nivo:
            trenutni_nivo = trenutni_nivo[deo]
            najbliza_putanja += "/" + deo
        else:
            return f"Fajl ne postoji. Najbliza postojeca putanja je: {najbliza_putanja}"

    naziv_servera = delovi[0]
    return server(naziv_servera, putanja)


zahtev = input("Unesi putanju fajla: ")

odgovor = middleware(zahtev)

print(odgovor)