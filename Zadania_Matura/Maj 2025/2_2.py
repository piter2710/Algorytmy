with open("symbole.txt") as f:
    linie = f.readlines()
    linie = [line.strip() for line in linie]
    znaki = 12
    linijki = len(linie)
    kwadraty = 0
    for i in range(linijki - 2):
        linia1 = linie[i]
        linia2 = linie[i + 1]
        linia3 = linie[i + 2]
        for j in range(znaki - 2):
            if (linia1[j] == linia1[j + 1] == linia1[j + 2] == linia2[j] == linia2[j + 1] == linia2[j + 2] == linia3[j] == linia3[j + 1] == linia3[j + 2]):
                print(f"Srodek: Numer wiersza {i + 1 + 1}, Numer pozycji w wierszu {j + 1 + 1}")
                #Dodatkowe +1 bo plik liczy wiersze i kolumny od 1 a nie od zera jak listy
                #print(f"{i+2} {j+2}")
                kwadraty += 1
    print(f"Liczba kwadratow: {kwadraty}")
    f.close()
    
