import threading
import time
import random

NUM_FILOSOFOS = 5

# Criando os talheres (locks)
talheres = [threading.Lock() for _ in range(NUM_FILOSOFOS)]

def filosofo(id):
    esquerdo = id
    direito = (id + 1) % NUM_FILOSOFOS

    # Prevenção de deadlock: ordenação de recursos
    primeiro = min(esquerdo, direito)
    segundo = max(esquerdo, direito)

    while True:
        print(f"Filósofo {id} está pensando 🤔")
        time.sleep(random.uniform(1, 3))

        print(f"Filósofo {id} tentou pegar o talher {primeiro}")
        with talheres[primeiro]:
            print(f"Filósofo {id} pegou o talher {primeiro}")

            print(f"Filósofo {id} tentou pegar o talher {segundo}")
            with talheres[segundo]:
                print(f"Filósofo {id} pegou o talher {segundo}")

                print(f"🍝 Filósofo {id} está comendo!")
                time.sleep(random.uniform(1, 2))

            print(f"Filósofo {id} devolveu o talher {segundo}")

        print(f"Filósofo {id} devolveu o talher {primeiro}")
        print("-" * 40)

def main():
    threads = []

    for i in range(NUM_FILOSOFOS):
        t = threading.Thread(target=filosofo, args=(i,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
