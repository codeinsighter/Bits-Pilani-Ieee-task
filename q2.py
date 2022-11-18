#1st pattern
a=65
b=70

size=b-a


i=0
tgl=0
while i<=size:
    j=a
    k=0
    while j<=b-i:
        print(chr(j),end='')
        j=j+1
    while k<2*i-1:
        print(' ',end='')
        k=k+1
    if i==0:
        j=b-i-1
    if i!=0:        
        j=b-i
    while j>=a:
        print(chr(j),end='')
        j=j-1
    if i==size:
        tgl=1
    if tgl:
        if i==0:
            break
        i=i-2
    i=i+1
    print(' ')
                       
            
        
print(' ')
print(' ')
print(' ')

#2nd pattern
n=7
print('*'*n)
for m in range(n-2):
    print(' '*(n-3-m),'*')
print('*'*n)