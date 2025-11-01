def czy_pierwsza(n):
    """Funkcja sprawdza, czy liczba n jest liczbą pierwszą.
    
    """
    
    if n <= 1:
        return False
    for i in range(2, n -1,1):
        if n % i == 0:
            return False
    return True

print("Czy liczba 29 jest pierwsza?", czy_pierwsza(29))
print("Czy liczba 15 jest pierwsza?", czy_pierwsza(15))
print("Czy liczba 1 jest pierwsza?", czy_pierwsza(1))
print("Czy liczba 2 jest pierwsza?", czy_pierwsza(2))
print("Czy liczba 97 jest pierwsza?", czy_pierwsza(97))
print("Czy liczba 100 jest pierwsza?", czy_pierwsza(100))