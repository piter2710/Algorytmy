# Szyfrowanie z Kluczem Publicznym (Asymetryczne)

## Podstawowe Pojęcia

Szyfrowanie asymetryczne, znane również jako **kryptografia klucza publicznego**, to metoda szyfrowania wykorzystująca **parę kluczy** matematycznie powiązanych:
- **Klucz publiczny** - może być swobodnie udostępniany
- **Klucz prywatny** - musi być zachowany w tajemnicy

## Zasada Działania

### 1. Generowanie Kluczy
- Użytkownik generuje parę kluczy: publiczny i prywatny
- Klucze są ze sobą matematycznie powiązane
- Znajomość klucza publicznego nie pozwala na odkrycie klucza prywatnego

### 2. Proces Szyfrowania
```
Tekst jawny + Klucz publiczny odbiorcy → Szyfrogram
```
- Nadawca używa **klucza publicznego odbiorcy** do zaszyfrowania wiadomości
- Każdy może zaszyfrować wiadomość dla danego odbiorcy

### 3. Proces Deszyfrowania
```
Szyfrogram + Klucz prywatny odbiorcy → Tekst jawny
```
- Tylko posiadacz **klucza prywatnego** może odszyfrować wiadomość
- Nawet nadawca nie może odszyfrować wysłanej wiadomości

## Własności Matematyczne

### Funkcje Jednokierunkowe z Klapką
Szyfrowanie asymetryczne opiera się na **funkcjach jednokierunkowych**:
- Łatwe do obliczenia w jednym kierunku
- Bardzo trudne do odwrócenia bez klucza prywatnego
- Możliwe do odwrócenia posiadając "klapkę" (klucz prywatny)

### Przykłady Trudnych Problemów Matematycznych
1. **Faktoryzacja** (RSA) - rozkład dużych liczb na czynniki pierwsze
2. **Problem logarytmu dyskretnego** (DSA, ElGamal)
3. **Krzywe eliptyczne** (ECC)

## Popularne Algorytmy

### RSA (Rivest-Shamir-Adleman)
- Najpopularniejszy algorytm asymetryczny
- Oparty na trudności faktoryzacji dużych liczb
- Używa dwóch dużych liczb pierwszych do generowania kluczy

### ECC (Elliptic Curve Cryptography)
- Kryptografia krzywych eliptycznych
- Zapewnia podobny poziom bezpieczeństwa przy krótszych kluczach
- Szybsza i bardziej efektywna niż RSA

### DSA (Digital Signature Algorithm)
- Głównie do podpisów cyfrowych
- Oparty na problemie logarytmu dyskretnego

## Zastosowania

### 1. Szyfrowanie Komunikacji
- Bezpieczna wymiana danych
- Każdy może wysłać zaszyfrowaną wiadomość używając klucza publicznego
- Tylko odbiorca może ją odszyfrować

### 2. Podpisy Cyfrowe
```
Dokument + Klucz prywatny nadawcy → Podpis
Podpis + Klucz publiczny nadawcy → Weryfikacja
```
- Potwierdzenie autentyczności nadawcy
- Zapewnienie integralności dokumentu
- Brak możliwości wyparcia się autorstwa

### 3. Wymiana Kluczy Symetrycznych
- Bezpieczne przesłanie klucza symetrycznego
- Hybrydowe systemy kryptograficzne (np. SSL/TLS)

### 4. Uwierzytelnianie
- Weryfikacja tożsamości użytkowników
- Systemy logowania bez hasła

## Zalety

✓ **Bezpieczna dystrybucja kluczy** - klucz publiczny może być swobodnie udostępniany  
✓ **Podpisy cyfrowe** - możliwość potwierdzenia autorstwa  
✓ **Nie wymaga bezpiecznego kanału** - do wymiany klucza publicznego  
✓ **Skalowalność** - n użytkowników potrzebuje n par kluczy (vs n²/2 w symetrycznym)

## Wady

✗ **Wolniejsze** - operacje matematyczne są bardziej złożone  
✗ **Większe klucze** - wymagają więcej pamięci (RSA: 2048-4096 bitów)  
✗ **Większe szyfrogramy** - zaszyfrowane dane są większe niż oryginał  
✗ **Zasoby obliczeniowe** - wymaga większej mocy obliczeniowej

## Przykład Praktyczny (RSA)

### Generowanie Kluczy
1. Wybierz dwie duże liczby pierwsze: p i q
2. Oblicz n = p × q (moduł)
3. Oblicz φ(n) = (p-1) × (q-1)
4. Wybierz e (wykładnik publiczny), gdzie 1 < e < φ(n) i NWD(e, φ(n)) = 1
5. Oblicz d (wykładnik prywatny), gdzie d × e ≡ 1 (mod φ(n))

**Klucz publiczny:** (n, e)  
**Klucz prywatny:** (n, d)

### Szyfrowanie
```
C = M^e mod n
```
gdzie M - wiadomość, C - szyfrogram

### Deszyfrowanie
```
M = C^d mod n
```

## Bezpieczeństwo

### Długość Klucza
- **RSA-2048** - minimalny standard
- **RSA-4096** - zwiększone bezpieczeństwo
- **ECC-256** - odpowiednik RSA-3072

### Zagrożenia
1. **Komputery kwantowe** - mogą złamać obecne algorytmy (algorytm Shora)
2. **Słabe generatory liczb losowych** - mogą prowadzić do przewidywalnych kluczy
3. **Ataki side-channel** - analiza czasu wykonania, zużycia energii

### Kryptografia postkwantowa
- Rozwój algorytmów odpornych na ataki kwantowe
- NIST prowadzi standaryzację nowych algorytmów

## Porównanie: Symetryczne vs Asymetryczne

| Cecha | Symetryczne | Asymetryczne |
|-------|-------------|--------------|
| **Klucze** | Jeden współdzielony | Para: publiczny + prywatny |
| **Szybkość** | Bardzo szybkie | Wolniejsze (10-1000x) |
| **Długość klucza** | 128-256 bitów | 2048-4096 bitów (RSA) |
| **Dystrybucja** | Wymaga bezpiecznego kanału | Klucz publiczny bez ochrony |
| **Użycie** | Szyfrowanie dużych danych | Wymiana kluczy, podpisy |
| **Przykłady** | AES, DES, 3DES | RSA, ECC, ElGamal |

## Systemy Hybrydowe

W praktyce często stosuje się **połączenie obu metod**:

1. **Szyfrowanie asymetryczne** - do wymiany klucza sesji
2. **Szyfrowanie symetryczne** - do szyfrowania właściwych danych

Przykład: **TLS/SSL**
- RSA/ECC do wymiany klucza
- AES do szyfrowania komunikacji

## Infrastruktura Klucza Publicznego (PKI)

### Certyfikaty Cyfrowe
- Potwierdzają przynależność klucza publicznego do właściciela
- Wystawiane przez zaufane organizacje (CA - Certificate Authority)
- Zapobiegają atakom "man-in-the-middle"

### Łańcuch Zaufania
```
Certyfikat główny (Root CA)
    ↓
Certyfikat pośredni (Intermediate CA)
    ↓
Certyfikat użytkownika końcowego
```

## Podsumowanie

Szyfrowanie z kluczem publicznym rozwiązuje kluczowy problem kryptografii symetrycznej - **bezpieczną wymianę kluczy**. Choć wolniejsze, jest fundamentem współczesnego bezpieczeństwa internetowego, umożliwiając bezpieczną komunikację między stronami, które nigdy wcześniej się nie kontaktowały.