n=int(input('Enter number of pairs to be inserted: '))

d={}
c={}

for i in range(0,n):
    key=input('Enter key:')
    value=input('Enter value corresponding to the above key: ')
    d[key]=value
print(d)
l=[]
h=int(input('Arrange key-wise(enter 1) or value-wise(enter 2) : '))

if h==1:
    for key in d:
        l.append((key,d[key]))
    l.sort()
    for i in l:
        c[i[0]]=i[1]
    print(l)
elif h==2:
    for key in d:
        l.append((d[key],key))
    l.sort()
    for i in l:
        c[i[0]]=i[1]
    print(c)
