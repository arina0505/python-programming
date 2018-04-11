a=int(input('enter the hr1'))
b=int(input('enter the min1'))
c=int(input('enter the hr2'))
d=int(input('enter the min2'))
x=a-c
y=b-d
if(x>0 and y>0):
    print(x,y)
else:
    print(-x,-y)
