"""Funkcja szybkie_potegowanie(a, n) oblicza a podniesione do potęgi n
   za pomocą metody szybkiego potęgowania.
   
   """

def szybkie_potegowanie(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:  # wykładnik parzysty
        temp = szybkie_potegowanie(a, n // 2)
        return temp * temp
    else:  # wykładnik nieparzysty
        return a * szybkie_potegowanie(a, n - 1)
"""
   Funkcja szybkie_potegowanie_iter(a, n) oblicza a podniesione do potęgi n
   za pomocą iteracyjnej metody szybkiego potęgowania.
   """ 
def szybkie_potegowanie_iter(a, n):
    wynik = 1
    podstawa = a
    
    while n > 0:
        if n % 2 == 1: # jeśli wykładnik jest nieparzysty
            wynik *= podstawa
        podstawa *= podstawa  # podnosimy podstawę do kwadratu
        n //= 2  # dzielimy wykładnik przez 2
    
    return wynik