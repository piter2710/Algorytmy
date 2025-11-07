def przestaw2(liczba):
    wynik = 0
    przesunięcie = 1
    while liczba > 0:
        dwie_cyfry = liczba % 100
        cyfra_dziesiatek = dwie_cyfry // 10 
        cyfra_jednosci = dwie_cyfry % 10 
        
        if liczba > 9:
            wynik = przesunięcie * cyfra_dziesiatek + 10 * przesunięcie * cyfra_jednosci + wynik
        else: 
            wynik = przesunięcie * cyfra_jednosci + wynik
        
        liczba = liczba // 100
        przesunięcie = przesunięcie * 100 
    
    return wynik
print(przestaw2(154005710))