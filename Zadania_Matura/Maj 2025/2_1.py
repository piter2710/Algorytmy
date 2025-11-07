with open("symbole.txt") as f:
    for line in f:
        if(line.strip() == line.strip()[::-1]):
            print(line)
    f.close()
