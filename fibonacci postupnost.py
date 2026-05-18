n = int(input('zadaj n-tý člen: '))
z=[1,2]
x=0
for i in range(2,n):
    x = z[-2] + z[-1]
    z.append(x)
print(z[-1])
    
    
