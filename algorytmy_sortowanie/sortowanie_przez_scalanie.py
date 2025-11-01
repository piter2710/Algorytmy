def merge_sort(tablica):
    n = len(tablica)
    if n <= 1:
        return tablica
    mid = n // 2
    left_half = merge_sort(tablica[:mid])
    right_half = merge_sort(tablica[mid:])
    return merge(left_half, right_half)
def merge(left, right):
    posortowana = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            posortowana.append(left[i])
            i += 1
        else:
            posortowana.append(right[j])
            j += 1
    posortowana.extend(left[i:])
    posortowana.extend(right[j:])
    return posortowana


def itterative_merge_sort(tablica):
    dlugosc_tablicy = len(tablica)
    
    # Zaczynamy od scalania par pojedynczych elementów
    aktualny_rozmiar = 1
    
    # Podwajamy rozmiar fragmentów w każdej iteracji (1 → 2 → 4 → 8 ...)
    while aktualny_rozmiar < dlugosc_tablicy:
        
        # Przechodzimy przez tablicę skokami co 2*aktualny_rozmiar
        # (bo scalamy 2 fragmenty wielkości aktualny_rozmiar)
        for lewy_start in range(0, dlugosc_tablicy, 2 * aktualny_rozmiar):
            
            # Obliczamy indeksy:
            # - koniec lewego fragmentu
            srodek = min(lewy_start + aktualny_rozmiar - 1, dlugosc_tablicy - 1)
            
            # - koniec prawego fragmentu
            prawy_koniec = min((lewy_start + 2 * aktualny_rozmiar - 1), (dlugosc_tablicy - 1))
            
            # Scalamy tylko jeśli istnieje prawy fragment
            if srodek < prawy_koniec:
                tablica[lewy_start:prawy_koniec + 1] = merge(
                    tablica[lewy_start:srodek + 1],      # lewy fragment
                    tablica[srodek + 1:prawy_koniec + 1] # prawy fragment
                )
        
        # Podwajamy rozmiar fragmentów do scalenia
        aktualny_rozmiar *= 2