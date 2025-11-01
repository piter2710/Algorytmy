def NWD(liczba1, liczba2):
    """Funkcja zwraca największy wspólny dzielnik dwóch liczb całkowitych dodatnich."""
    while liczba1 != liczba2:
        if liczba1 > liczba2:
            liczba1 -= liczba2
        else:
            liczba2 -= liczba1
    return liczba1

def NWW(liczba1, liczba2):
    """Funkcja zwraca najmniejszą wspólną wielokrotność dwóch liczb całkowitych dodatnich."""
    return (liczba1 * liczba2) // NWD(liczba1, liczba2)

print("NWW liczb 358 i 486 wynosi:", NWW(358, 486) , "\nNWD liczb 358 i 486 wynosi:", NWD(358, 486))