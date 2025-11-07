def czy_w_kwadracie(x, y):
    if(x >= 5000 or x <= 0):
        return False
    if(y >= 5000 or y <= 0):
        return False
    return True
def czySrodek(P1,P2,P3):
    x1, y1 = P1
    x2, y2 = P2
    x3, y3 = P3
    return (x2 == (x1 + x3) / 2) and (y2 == (y1 + y3) / 2)

with open ("dron.txt") as f:
    odleglosc = 0
    wysokosc = 0
    
    
    dane = []
    wykres = []
    c = 0
    for line in f:
        num1, num2 = map (int, line.split())
        dane.append((num1,num2))
    
    for dana in dane:
        odleglosc += dana[0]
        wysokosc += dana[1]
        wykres.append((odleglosc, wysokosc))
    #Punkt A
    for dana in wykres:
        if czy_w_kwadracie(dana[0], dana[1]):
            c += 1
    print(c)
    print("-----")
    
    #Punkt B
    
    for i in range(len(wykres)):
        for j in range(i+1, len(wykres)):
            for k in range(j+1, len(wykres)):
                if czySrodek(wykres[i], wykres[j], wykres[k]):
                    print(wykres[j], " jest srodkiem miedzy ", wykres[i], " a ", wykres[k])
    
    
        
    