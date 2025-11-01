def pierwiastek_polowienie(liczba, dokladnosc=1e-10):
    """
    Oblicza pierwiastek kwadratowy z liczby metodą połowienia (bisekcji).
    
    Args:
        liczba: liczba, z której obliczamy pierwiastek (liczba >= 0)
        dokladnosc: dokładność obliczeń (domyślnie 1e-10)
    
    Returns:
        Przybliżona wartość pierwiastka kwadratowego z liczby
    """
    if liczba < 0:
        raise ValueError("Nie można obliczyć pierwiastka z liczby ujemnej")
    
    if liczba == 0:
        return 0
    
    # Ustalenie przedziału początkowego [poczatek_przedzialu, koniec_przedzialu]
    if liczba >= 1:
        poczatek_przedzialu = 0
        koniec_przedzialu = liczba
    else:  # dla liczb między 0 a 1, pierwiastek jest większy od liczby
        poczatek_przedzialu = liczba
        koniec_przedzialu = 1
    
    # Metoda połowienia (bisekcji)
    while koniec_przedzialu - poczatek_przedzialu > dokladnosc:
        srodek_przedzialu = (poczatek_przedzialu + koniec_przedzialu) / 2
        kwadrat_srodka = srodek_przedzialu * srodek_przedzialu
        
        if kwadrat_srodka > liczba:
            # Pierwiastek jest w lewej połowie przedziału
            koniec_przedzialu = srodek_przedzialu
        else:
            # Pierwiastek jest w prawej połowie przedziału
            poczatek_przedzialu = srodek_przedzialu
    
    # Zwracamy środek ostatniego przedziału jako wynik
    wynik = (poczatek_przedzialu + koniec_przedzialu) / 2
    return wynik


# Przykłady użycia
if __name__ == "__main__":
    import math
    
    print("=== Algorytm pierwiastka kwadratowego metodą połowienia ===\n")
    
    # Test dla różnych liczb
    liczby_testowe = [2, 4, 9, 16, 25, 100, 0.25, 0.5, 1000]
    
    for liczba in liczby_testowe:
        wynik = pierwiastek_polowienie(liczba)
        wynik_wbudowany = math.sqrt(liczba)
        blad = abs(wynik - wynik_wbudowany)
        
        print(f"√{liczba:7.2f} = {wynik:.10f}")
        print(f"  math.sqrt: {wynik_wbudowany:.10f}")
        print(f"  błąd:      {blad:.2e}\n")
