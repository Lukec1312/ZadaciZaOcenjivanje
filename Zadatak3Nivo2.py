fajl_sistem = {
    "server1": {
        "data": {
            "folder": {
                "file.txt": "Ovo je sadrzaj fajla file.txt"
            }
        }
    },
    "server2": {
        "data": {
            "slike": {
                "slika.jpg": "Ovo je slika"
            }
        }
    }
}


def server(naziv_servera, putanja):
    return f"{naziv_servera} vraca fajl: {putanja}"


def middleware(trazena_putanja):
    delovi = trazena_putanja.strip("/").split("/")

    trenutni_nivo = fajl_sistem
    postojeca_putanja = ""

    for deo in delovi:
        if deo in trenutni_nivo:
            trenutni_nivo = trenutni_nivo[deo]
            postojeca_putanja += "/" + deo
        else:
            return f"Fajl ne postoji. Najbliza postojeca putanja je: {postojeca_putanja}"

    server_ime = delovi[0]
    return server(server_ime, trazena_putanja)


zahtev = input("Unesi putanju fajla: ")

odgovor = middleware(zahtev)

print(odgovor)