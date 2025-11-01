def rozkład_na_czynniki_pierwsze(liczba):
    """Zwraca listę czynników pierwszych danej liczby."""
    czynniki = []
    i = 2
    while i * i <= liczba:
        while (liczba % i) == 0:
            czynniki.append(i)
            liczba //= i
        i += 1
    if liczba > 1:
        czynniki.append(liczba)
    return czynniki

print("Rozkład na czynniki pierwsze liczby 360:", rozkład_na_czynniki_pierwsze(360))