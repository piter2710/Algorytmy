def decimal_to_base3(n):
    if n == 0:
        return "0"
    digits = []
    while n > 0:
        digits.append(str(n % 3))
        n //= 3
    return "".join(digits[::-1])
with open("przyklad.txt") as f:
    wyniki = []
    for lane in f:
        wynik = ""
        for letter in lane:
            if(letter == "+"):
                wynik+="1"
            elif(letter == "*"):
                wynik+="2"
            elif(letter == "o"):
                wynik+="0"
        wyniki.append(wynik)
    wyniki = [int(x, 3) for x in wyniki]
    wynik_final = max(wyniki)
    print(wynik_final)
    f.close()