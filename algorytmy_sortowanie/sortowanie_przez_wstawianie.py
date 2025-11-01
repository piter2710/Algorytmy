def insert_sort(tablica):
    n = len(tablica)
    
    # Zaczynamy od drugiego elementu (indeks 1), bo pierwszy jest już "posortowany"
    for i in range(1, n):
        # KLUCZ = element, który aktualnie wstawiamy w odpowiednie miejsce
        klucz = tablica[i]
        
        # j = pozycja poprzedniego elementu (zaczynamy sprawdzać od tyłu)
        j = i - 1
        
        # Cofamy się w lewo i przesuwamy elementy większe od klucza w prawo
        # Robimy to dopóki: 1) nie wyjdziemy poza tablicę (j >= 0)
        #                   2) element jest większy od klucza
        while j >= 0 and tablica[j] > klucz:
            tablica[j + 1] = tablica[j]  # Przesuwamy element w prawo
            j -= 1  # Idziemy dalej w lewo
        
        # Wstawiamy klucz na odpowiednie miejsce (tam gdzie przestaliśmy)
        tablica[j + 1] = klucz
    
    return tablica

# Przykładowe użycie
lista = [64, 34, 25, 12, 22, 11, 90]
posortowana_lista = insert_sort(lista)
print("Posortowana lista:", posortowana_lista)

"""
=== JAK DZIAŁA SORTOWANIE PRZEZ WSTAWIANIE ===

Wyobraź sobie sortowanie kart w ręku:
1. Bierzemy pierwszą kartę - jest już "posortowana"
2. Bierzemy drugą kartę (to jest KLUCZ) i sprawdzamy czy jest mniejsza od pierwszej
   - Jeśli TAK: przesuwamy pierwszą w prawo i wstawiamy drugą na jej miejsce
   - Jeśli NIE: zostawiamy na miejscu
3. Bierzemy trzecią kartę (nowy KLUCZ) i cofamy się w lewo, porównując:
   - Jeśli klucz jest mniejszy od poprzednich kart, przesuwamy je w prawo
   - Zatrzymujemy się, gdy znajdziemy właściwe miejsce
4. Wstawiamy klucz na znalezione miejsce
5. Powtarzamy dla kolejnych kart

PRZYKŁAD KROK PO KROKU dla [64, 34, 25]:
Start:     [64, 34, 25]
           
Krok 1: i=1, klucz=34
  - 64 > 34? TAK → przesuń 64 w prawo
  - Wstaw 34 na początku
  Wynik:   [34, 64, 25]
  
Krok 2: i=2, klucz=25
  - 64 > 25? TAK → przesuń 64 w prawo → [34, 64, 64]
  - 34 > 25? TAK → przesuń 34 w prawo → [34, 34, 64]
  - Koniec tablicy, wstaw 25 na początku
  Wynik:   [25, 34, 64]

"""