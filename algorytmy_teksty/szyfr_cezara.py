def szyfr_cezara(tekst, klucz):
    zaszyfrowany_tekst = ""
    
    for znak in tekst:
        #Tylko teksty literowe są szyfrowane
        if znak.isalpha():
            #chr oznacza konwersję z kodu ASCII na znak - chr(65) = 'A'
            #ord oznacza konwersję z znaku na kod ASCII - ord('A') = 65
            #Modulo 26 zapewnia zawinięcie się alfabetu po 26 literach
            
            # Sprawdzamy czy znak jest wielką literą
            if znak.isupper():
                # Dla wielkich liter: zakres A-Z (65-90)
                przesuniety_znak = chr((ord(znak) - ord('A') + klucz) % 26 + ord('A'))
            else:
                # Dla małych liter: zakres a-z (97-122)
                przesuniety_znak = chr((ord(znak) - ord('a') + klucz) % 26 + ord('a'))
            
            zaszyfrowany_tekst += przesuniety_znak
        else:
            zaszyfrowany_tekst += znak
    
    return zaszyfrowany_tekst

def odszyfruj_cezara(zaszyfrowany_tekst, klucz):
    return szyfr_cezara(zaszyfrowany_tekst, -klucz)

# Przykłady użycia
if __name__ == "__main__":
    oryginalny_tekst = "Ala ma !kota!"
    klucz = 3
    zaszyfrowany = szyfr_cezara(oryginalny_tekst, klucz)
    odszyfrowany = odszyfruj_cezara(zaszyfrowany, klucz)
    
    print("Oryginalny tekst: ", oryginalny_tekst)
    print("Zaszyfrowany tekst:", zaszyfrowany)
    print("-----------------------------------")
    print("Odszyfrowany tekst:", odszyfrowany)