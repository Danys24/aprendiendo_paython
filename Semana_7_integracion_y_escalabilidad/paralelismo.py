from multiprocessing import Process, cpu_count
import time

def contador(num):
    cont = 0
    while cont < num:
        cont += 1

def main(): 
    iniciar = time.perf_counter()

    a = Process(target=contador, args=(200000000,))
    b = Process(target=contador, args=(200000000,))
    c = Process(target=contador, args=(100000000,))
    d = Process(target=contador, args=(100000000,))
    e = Process(target=contador, args=(100000000,))
    f = Process(target=contador, args=(100000000,))
    g = Process(target=contador, args=(100000000,))
    h = Process(target=contador, args=(100000000,))

    a.start()
    b.start()
    c.start()
    d.start()
    e.start()
    f.start()
    g.start()
    h.start()

    a.join()
    b.join()
    c.join()
    d.join()
    e.join()
    f.join()
    g.join()
    h.join()

    fin = time.perf_counter()

    print(f"El tiempo del proceso es: {fin - iniciar}")
    print(cpu_count())

if __name__ == '__main__':
    main()