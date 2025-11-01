def bubble_sort(tablica):
    n = len(tablica)
    for i in range(n):
        for j in range(n-1-i):
            if tablica[j] > tablica[j+1]:
                temp = tablica[j]
                tablica[j] = tablica[j+1]
                tablica[j+1] = temp
    return tablica

# Przykładowe użycie
lista = [64, 34, 25, 12, 22, 11, 90]
posortowana_lista = bubble_sort(lista)
print("Posortowana lista:", posortowana_lista)

"""Teoria:
Sortowanie bąbelkowe to prosty algorytm sortowania, który działa poprzez wielokrotne przechodzenie przez listę,
porównywanie sąsiednich elementów i zamienianie ich miejscami, jeśli są w niewłaściwej kolejności. 
Proces ten jest powtarzany aż do momentu, gdy lista jest posortowana."""

