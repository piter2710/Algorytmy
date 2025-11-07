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
result1, counter1 = przestaw(316498)
result2, counter2 = przestaw(43657688)
result3, counter3 = przestaw(154005710)
result4, counter4 = przestaw(998877665544321)
def Wynik(result, counter):
    print(f"Wynik: {result}")
    print(f"Wywolana {counter}")
Wynik(result1,counter1)
Wynik(result2,counter2)
Wynik(result3,counter3)
Wynik(result4,counter4)