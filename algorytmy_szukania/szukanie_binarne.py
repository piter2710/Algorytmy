def binary_search(posortowana_tablica, szukana_wartosc):
    lewy = 0
    prawy = len(posortowana_tablica) - 1
    while lewy <= prawy:
        srodek = (lewy + prawy) // 2
        if posortowana_tablica[srodek] == szukana_wartosc:
            return srodek
        elif posortowana_tablica[srodek] < szukana_wartosc:
            lewy = srodek + 1
        else:
            prawy = srodek - 1
    return -1


# Przykładowe użycie
posortowana_lista = [1, 3, 5, 7, 9, 11, 13, 15]
szukana_wartosc1 = 7
indeks1 = binary_search(posortowana_lista, szukana_wartosc1)
print("Element {} znaleziony na indeksie: {}".format(szukana_wartosc1, indeks1))

"""Teoria:
Wyszukiwanie binarne to efektywny algorytm służący do znajdowania pozycji określonej wartości w posortowanej tablicy.
Działa na zasadzie dzielenia tablicy na pół i porównywania środkowego elementu z szukaną wartością.
1. Na początku ustalamy dwa wskaźniki: lewy (początek tablicy) i prawy (koniec tablicy).
2. Obliczamy indeks środkowego elementu tablicy.
3. Porównujemy środkowy element z szukaną wartością:
   - Jeśli są równe, zwracamy indeks środkowego elementu.
   - Jeśli szukana wartość jest mniejsza, przesuwamy prawy wskaźnik na lewo od środka.
   - Jeśli szukana wartość jest większa, przesuwamy lewy wskaźnik na prawo od środka.
4. Powtarzamy kroki 2-3, aż znajdziemy wartość lub lewy wskaźnik przekroczy prawy (co oznacza, że wartość nie istnieje w tablicy). """