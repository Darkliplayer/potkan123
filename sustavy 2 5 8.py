a = int(input('zadaj číslo: '))
b=bin(a)[2:]
o=oct(a)[2:]
if a == 0:
    pen+=0
pen = ''
while a>0:
    pen = str(a%5)+pen
    a//=5
print('2ková: '+b)
print('5-kova: '+pen)
print('8kova: '+o)
