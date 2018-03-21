x=int(input('enter the num1'))
y=int(input('enter the num2'))
for i in range(x,y+1):
    x1=len(str(i))
    n=i
    sum=0
    while(n>0):
      a=n%10
      b=a**x1
      sum=sum+b
      n=n//10
    if(i==sum):
      print(i)
