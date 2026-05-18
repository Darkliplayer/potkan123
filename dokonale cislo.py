x = int(input('zadaj čislo: '))
a=0
n=0
for i in range (1,x):
    if x%int(i)==0:
        a = a+i
if x == a:
    print('dokonaké číslo')
