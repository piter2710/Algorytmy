
def porownaj_teksty(tekst1, tekst2):
    return tekst1 == tekst2
print(porownaj_teksty("Ala ma kota", "Ala ma kota"))  # True
print(porownaj_teksty("Ala ma kota", "Ala ma psa"))   # False
print(porownaj_teksty("Hello, World!", "Hello, World!!")) # False