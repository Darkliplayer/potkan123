import random
m=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
v=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
a=random.choice(m)
b=random.choice(m)
c=random.randint(1,11)
d=random.randint(1,11)
e=random.choice(v)
f=random.choice(v)
g=random.randint(1,11)
h=random.randint(1,11)
print(a+b+str(c)+str(d)+e+f+str(g)+str(h))
