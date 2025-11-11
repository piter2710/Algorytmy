#Zadanie 3.1
def Nieparzysty_skrot(n):

    m = 0
    p = 1
    czy_istnieje = False
    while(n > 0):
        ostatnia_cyfra = n % 10
        if(ostatnia_cyfra % 2 != 0):
            m = ostatnia_cyfra * p + m
            p*=10
            czy_istnieje = True
        n = n // 10
    if czy_istnieje:
        return m
    return False
#   return 'Nie istnieje skrot tej liczby'
print(Nieparzysty_skrot(123))

# Zadanie 3.2
with open("skrot.txt") as f:
    wszystkie_liczby = f.readlines()
    liczby = list(map(lambda x: int(x.strip()), wszystkie_liczby))


    bezSkrotu = []
    for liczba in liczby:
        skrot = Nieparzysty_skrot(liczba)
        if not skrot:
            bezSkrotu.append(liczba)
    print(max(bezSkrotu), len(bezSkrotu))
    f.close()

#Zadanie 3,3
def NWD(a,b):
    while(a != b):
        if(a > b):
            a = a -b
        else:
            b = b -a
    return a
with open("skrot2.txt") as f:
    wszystkie_liczby = f.readlines()
    liczby = list(map(lambda x: int(x.strip()), wszystkie_liczby))
    liczby_nwd = []
    for liczba in liczby:
        if NWD(liczba,Nieparzysty_skrot(liczba)) == 7:
            liczby_nwd.append(liczba)
    print(liczby_nwd)