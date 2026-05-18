x = input('zadaj text: ')
more = list(x)
a= -1
p = int(input('posun: '))
slovo = ''
for i in more:
    a = a+1
    print(more)
    ch = ord(more[a])
    ch = ch + p 
    ans = chr(ch)
    slovo = slovo + ans
print(slovo)
    
