import random
p=0
n=0
s=[]
for i in range(1,31):
    a = random.randint(1,101)
    print(a)
    if a%7==0:
        s.append(str(a))
    if a % 2:
        p=p+1
    else:
        n=n+1
print('počet párnych čísel: ',p)
print('počet párnych čísel: ',n)
print('čísla deliteľné 7mou: ',s)
        
    
