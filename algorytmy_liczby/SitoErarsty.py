def sito_eratostenesa(n):
    """Funkcja zwraca listę liczb pierwszych mniejszych lub równych n
    za pomocą sita Eratostenesa.
    """
    if n < 2:
        return []

    # Inicjalizacja listy liczb od 2 do n
    liczby = list(range(2, n + 1))
    
    # Sito Eratostenesa
    # Dla 2 - zachowaj 2 i pomin wszystko, co jest wielokrotnością 2
    #Dla 3 - zachowaj 3 i pomin wszystko, co jest wielokrotnością 3
    #Dla 4 już nie istnieje, bo zostało pominięte jako wielokrotność 2
    #Dla 5 - zachowaj 5 i pomin wszystko, co jest wielokrotnością 5
    for i in range(2, int(n**0.5) + 1):
        #Filtrowanie liczb do nowej listy
        liczby = [x for x in liczby if x == i or x % i != 0]
    return liczby

print("Liczby pierwsze mniejsze lub równe 50:", sito_eratostenesa(50))
print("Liczby pierwsze mniejsze lub równe 100:", sito_eratostenesa(100))
print("Liczby pierwsze mniejsze lub równe 150:", sito_eratostenesa(150))
print("Liczby pierwsze mniejsze lub równe 200:", sito_eratostenesa(200))
print("Liczby pierwsze mniejsze lub równe 250:", sito_eratostenesa(250))
