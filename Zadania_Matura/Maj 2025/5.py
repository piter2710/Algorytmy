# ZROBIONE Z NUDÓW, NAJLEPIEJ TO POPROSTU PISEMNIE ROZWIĄZAĆ I TYLE
# TUTAJ TYLKO CHCIAŁEM SPRAWDZIĆ JAK TRUDNE JEST TO DO ZROBIENIA W KODZIE
# I TAK SZCZERZE SIE NIE OPLACA

def binarny_do_dziesietnego(n):
    return int(str(n), 2)
# 11X010110X1 0,,0 0,1 1,0 1,1
liczba1_mozliwosc = ['11001011001', '11001011011', '11101011001', '11101011011']

liczby1_dziesietne = [binarny_do_dziesietnego(liczba) for liczba in liczba1_mozliwosc]

liczby2_mozliwosc = ['1100010111', '1100110111']
liczby2_dziesietne = [binarny_do_dziesietnego(liczba) for liczba in liczby2_mozliwosc]

print(liczby1_dziesietne, liczby2_dziesietne)
# 1X011001XX10 0,0,0 0,0,1 0,1,0 0,1,1 1,0,0 1,0,1 1,1,0 1,1,1
liczby3_mozliwosc = [
    '100110010010', '100110010011', '100110010100', '100110010101',
    '100110011010', '100110011011', '100110011100', '100110011101'
]
liczby3_dziesietne = [binarny_do_dziesietnego(liczba) for liczba in liczby3_mozliwosc]

for l1 in liczby1_dziesietne:
    for l2 in liczby2_dziesietne:
        if (l1 + l2) in liczby3_dziesietne:
            print(l1,liczba1_mozliwosc[liczby1_dziesietne.index(l1)], l2,liczby2_mozliwosc[liczby2_dziesietne.index(l2)], l1 + l2, liczby3_mozliwosc[liczby3_dziesietne.index(l1 + l2)])
            
#ODPOWIEDZ:

# 11001011011 + 1100110111 = 100110010010

  