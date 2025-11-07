def decimal_to_base3(n):
    if n == 0:
        return "0"
    digits = []
    while n > 0:
        digits.append(str(n % 3))
        n //= 3
    return "".join(digits[::-1])



mapping = {'+': '1', '*': '2', 'o': '0'}
inv_mapping = {'0': 'o', '1': '+', '2': '*'}

wyniki = []
with open("symbole.txt") as f:
    for lane in f:
        lane = lane.strip()  
        if not lane:
            continue
        liczba_str = []
        for ch in lane:
            if ch in mapping:
                liczba_str.append(mapping[ch])
        if liczba_str:
            wyniki.append("".join(liczba_str))
ints = [int(s, 3) for s in wyniki]
wynik_final = sum(ints)

trojkowy = decimal_to_base3(wynik_final)

znaki = "".join(inv_mapping[d] for d in trojkowy)

print(wynik_final)
print(znaki)
f.close()