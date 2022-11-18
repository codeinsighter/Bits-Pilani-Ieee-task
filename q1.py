cases=int(input('Enter no. of test cases: '))
for i in range(0,cases):
    x=input('Enter string of even lenght : ')
l=len(x)
e=l//2
d=e
f=l


if l%2==0:
    p=x[0:d]
    q=x[e:f]
else:
    print('Error')
a=input('Enter first part:')
b=input('Enter second part:')


z=a+b


if x==z:
    print('yes')
else:
    print('no')
