s = str(input('zadaj slovo: '))
s = s.replace(' ','')
x = s[::-1]
if x ==s:
    print('slovo je palindrom')
else:
    print('slovo nie je palindrom')
