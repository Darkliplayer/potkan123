text=input("Zadaj text na zašifrovanie: ").lower()
posunutie = int(input("Zadaj posun: "))
posun = []
for i in text:
    print(ord(i))
    if (ord(i) + posunutie) > ord("z"):
        posun.append((ord(i) + posunutie)-123+97)
    else:
        posun.append(ord(i) + posunutie)

for i in posun:
    print(chr(i),end="")
