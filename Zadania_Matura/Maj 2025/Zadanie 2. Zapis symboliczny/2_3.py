mapping = {'+': '1', '*': '2', 'o': '0'}

values = []
with open("symbole.txt", encoding="utf-8") as f:
    lines = [line.strip() for line in f]

for line in lines:
    converted = ''.join(mapping[ch] for ch in line if ch in mapping)
    if not converted:
        continue
    values.append(int(converted, 3))

if values:
    print(max(values), lines[values.index(max(values))])
f.close()
