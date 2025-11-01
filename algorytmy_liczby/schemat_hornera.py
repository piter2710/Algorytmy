def schemat_hornera(wspolczynniki, x):
    """Funkcja schemat_hornera(wspolczynniki, x) oblicza wartość wielomianu
       dla danego x za pomocą schematu Hornera.
       
       Argumenty:
       wspolczynniki -- lista współczynników wielomianu, gdzie
                        wspolczynniki[i] to współczynnik przy x^i
       x -- punkt, w którym obliczana jest wartość wielomianu
       
       Zwraca:
       Wartość wielomianu w punkcie x.
    """
    wynik = 0
    for wspolczynnik in reversed(wspolczynniki):
        wynik = wynik * x + wspolczynnik
    return wynik

