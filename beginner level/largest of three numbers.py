x=int(input('enter the num1'))
y=int(input('enter the num2'))
z=int(input('enter the num3'))
if(x>y):
    if(x>z):
        print('x is largest')
    else:
        print('z is largest')
else:
    if(y>z):
        print('y is largest')
    else:
        print('z is largest')
