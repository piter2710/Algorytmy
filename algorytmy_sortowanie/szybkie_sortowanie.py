def szybkie_sortowanie(tablica):
    if len(tablica) <= 1:
        return tablica
    
    pivot = tablica[len(tablica) // 2]
    lewa = [x for x in tablica if x < pivot]
    srodkowa = [x for x in tablica if x == pivot]
    prawa = [x for x in tablica if x > pivot]
    
    return szybkie_sortowanie(lewa) + srodkowa + szybkie_sortowanie(prawa)