n=int(input('enter the number'))
a=0
b=1 
for i in range(n):
    if(i<=1):
        next=i
    else:
        next=a+b
        a=b
        b=next 
    i=i+1    
    print(next)
