class roman:
    def __init__(self, value):
        b=a//1000
        if b<=3:
            print('M'*b,end='')
        else:
            print('invalid input')

        c=a%1000
        d=c//100
        if d==9:
            print('CM',end='')
        if d>5 and d!=9:
            print('D'+'C'*(d-5),end='')
        if d==5:
            print('D',end='')
        if d==4:
            print('CD',end='')
        if d==0:
            pass
        if d<4:
            print('C'*d,end='')
            
        c=a%100
        d=c//10
        if d==9:
            print('XC',end='')
        if d>5 and d!=9:
            print('L'+'X'*(d-5),end='')
        if d==5:
            print('L',end='')
        if d==4:
            print('XL',end='')
        if d==0:
            pass
        if d<4:
            print('X'*d,end='')
            
        d=a%10
        if d==9:
            print('IX',end='')
        if d>5 and d!=9:
            print('V'+'I'*(d-5),end='')
        if d==5:
            print('V',end='')
        if d==4:
            print('IV',end='')
        if d==0:
            pass
        if d<4:
            print('I'*d,end='')

        print('')    

a = int(input('enter any number below 4000 : '))
weed = roman(a)