import time

def interceptor(func):
    def wrapper():
        start = time.time()

        func()

        end = time.time()
        print("Vreme izvrsavanja:", end - start, "sekundi")

    return wrapper


@interceptor
def neka_funkcija():
    print("Funkcija se izvrsava...")
    time.sleep(2)


neka_funkcija()