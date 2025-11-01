def wyszukiwanie_wzorca(tekst, wzorzec):
    n = len(tekst)
    m = len(wzorzec)
    
    for i in range(n - m + 1):
        j = 0
        while j < m and tekst[i + j] == wzorzec[j]:
            j += 1
        if j == m:
            return i
    return -1

# Przykładowe użycie
tekst1 = "KOT KOCHA WYCHODZIĆ NA SPACER Z WŁAŚNIEKIM ANDRZEJEM"
wzorzec1 = "ANDRZEJEM"
wzorzec2 = "MARIA"
wzorzec3 = "SPACER"
print("Wzorzec1 '{}' znaleziony na pozycji: {}".format(wzorzec1, wyszukiwanie_wzorca(tekst1, wzorzec1)))
print("Wzorzec2 '{}' znaleziony na pozycji: {}".format(wzorzec2, wyszukiwanie_wzorca(tekst1, wzorzec2)))
print("Wzorzec3 '{}' znaleziony na pozycji: {}".format(wzorzec3, wyszukiwanie_wzorca(tekst1, wzorzec3)))

