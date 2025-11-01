def szukanie_liniowe(tablica, cel):
    n = len(tablica)
    
    for i in range(n):
        if tablica[i] == cel:
            return i  
    
    return -1

# Przykładowe użycie
lista = [4, 2, 5, 1, 3]
element_do_znalezienia = 3
indeks = szukanie_liniowe(lista, element_do_znalezienia)

print("Element {} znaleziony na indeksie: {}".format(element_do_znalezienia, indeks))