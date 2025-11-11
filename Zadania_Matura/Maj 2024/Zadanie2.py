#Zadanie 2.1
def Cyfry(n):
    b= 1
    c = 0
    ilosc = 0
    while n > 0:
        a = n % 10
        n = n // 10
        if a % 2 == 0:
            c = c + b * (a // 2)
        else:
            c = c + b
            ilosc +=1
        b = b * 10
    return c, ilosc
print(Cyfry(33658))
print(Cyfry(542102))
print(Cyfry(87654321012345678))

#Zadanie 2.2
print(Cyfry(333333666666999999))

