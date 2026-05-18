import random
a = random.randint(1,6)
b = random.randint(1,6)
c = random.randint(1,6)
print(a)
print(b)
print(c)
if a==b==c:
    print('VÝHRA')
else:
    if a==b or a==c or b==c:
        print('SKORO')
    else:
        print('PREHRA')
