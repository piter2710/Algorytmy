def przestaw(n, counter=1):
    r = n % 100
    a = r // 10
    b = r % 10
    n = n // 100
    
    if n > 0:
        w, counter = przestaw(n, counter + 1)
        w = a + 10 * b + 100 * w
    else:
        if a > 0:
            w = a + 10 * b
        else:
            w = b

    return w, counter

def Wynik(result, counter):
    print(f"Wynik: {result}")
    print(f"Wywolana {counter}")

def zalezne_od_k(l, k):
    liczba = l * (10 ** (k -1))
    przestawiona, counter = przestaw(liczba)
    print(f"liczba {k} cyfrowa: ")
    Wynik(przestawiona, counter)
    
zalezne_od_k(1,20)
zalezne_od_k(1,21)
zalezne_od_k(1,22)
zalezne_od_k(1,23)