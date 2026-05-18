with open('subor.txt','r') as z:
    s = z.read()
l = len(s)
k=s.count('k')
mk=s.replace('k','m')
print('poČet znakov: ',l)
print('počet písmen k:',k)
print('pôvodný text: ',s)
print('upravený text:',mk)
