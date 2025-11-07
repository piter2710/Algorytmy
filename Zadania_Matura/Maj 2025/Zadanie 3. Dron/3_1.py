def NWD(liczba1, liczba2):
    if liczba1 == 0:
        return liczba2
    if liczba2 == 0:
        return liczba1
    while(liczba1 != liczba2):
        if(liczba2 > liczba1):
            liczba2 = liczba2 - liczba1
        else:
            liczba1 = liczba1 - liczba2
    return liczba1


with open ("dron.txt") as f:
    dane = []
    c = 0
    for line in f:
        num1, num2 = map (int, line.split())
        dane.append(NWD(abs(num1), abs(num2)))
    for dana in dane:
        if (dana > 1):
            c += 1
    print(c)
    f.close()
    