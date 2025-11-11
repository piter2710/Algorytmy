with open("liczby.txt") as f:
    pierwszy_rzad = f.readline()
    drugi_rzad = f.readline()
    liczby1 = [int(x) for x in pierwszy_rzad.split()]
    liczby2 = [int(x) for x in drugi_rzad.split()]

    #Zadanie 4.1
    ile_dzielnikow = 0
    for i in liczby1:
        for j in liczby2:
            if j % i ==0:
                ile_dzielnikow +=1
                break
    print(ile_dzielnikow)

    #Zadanie 4.2
    liczby1_sort = [int(x) for x in pierwszy_rzad.split()]
    liczby1_sort.sort()
    liczby1_sort = liczby1_sort[::-1]
    print(liczby1_sort[100])

    #Zadanie 4.3
def Rozklad(liczba):
    czynniki = []
    dzielnik = 2
    while (liczba > 1):
            if liczba % dzielnik == 0:
                liczba = liczba // dzielnik
                czynniki.append(dzielnik)
            else:
                dzielnik +=1
    return czynniki
print(Rozklad(12))
czyPoprawne = True
poprawne_liczby = []
for liczba in liczby2:
    czyPoprawne = True
    rozk = Rozklad(liczba)
    for roz in rozk:
        k = liczby1.count(roz)
        l = rozk.count(roz)

        if(k == 0 or k < l):
            czyPoprawne = False
    if czyPoprawne:
        poprawne_liczby.append(liczba)

print(poprawne_liczby)
max_srednia = -1
dlugosc_ciagu = -1
pierwszy_element = -1
#Zadanie 4.4
for i in range(0,len(liczby1) - 49):
    suma = sum(liczby1[i:i+50])
    for j in range(50, len(liczby1) - i + 1):
        if j > 50:
            suma = suma + liczby1[j + i -1]
        srednia = suma / j
        if srednia > max_srednia:
            max_srednia = srednia
            dlugosc_ciagu = j
            pierwszy_element = liczby1[i]
print(max_srednia,dlugosc_ciagu,pierwszy_element)