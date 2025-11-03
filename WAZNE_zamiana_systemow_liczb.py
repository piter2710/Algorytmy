def convert_to_system(liczba,system):
    if liczba == 0:
        return "0"
    wynik =""
    liczby = "0123456789ABCDEF"
    
    while(liczba > 0):
        reszta = liczba % system
        wynik = liczby[reszta] + wynik
        liczba //= system
    return wynik
