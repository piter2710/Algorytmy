dec_numbers = [15, 12, 2, 4, 7, 8]

# Konwersja z dziesiętnego na binarne
dec_TO_bin = []
for i in dec_numbers:
    dec_TO_bin.append(bin(i)[2:])

# Konwersja z dziesiętnego na ósemkowe
dec_to_oct = []
for i in dec_numbers:
    dec_to_oct.append(oct(i)[2:])

# Konwersja z dziesiętnego na heksadecymalne
dec_to_hex = []
for i in dec_numbers:
    dec_to_hex.append(hex(i)[2:])

# Konwersja z binarnego na dziesiętne
bin_to_dec = []
for i in dec_TO_bin:
    bin_to_dec.append(int(i, 2))

# Konwersja z ósemkowego na dziesiętne
oct_to_dec = []
for i in dec_to_oct:
    oct_to_dec.append(int(i, 8))

# Konwersja z heksadecymalnego na dziesiętne
hex_to_dec = []
for i in dec_to_hex:
    hex_to_dec.append(int(i, 16))

print(dec_to_hex)