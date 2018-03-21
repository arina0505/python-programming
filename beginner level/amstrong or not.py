n=int(input('enter the number'))
temp=n
sum=0
if(n<=100000):
 while(temp>0):
    a=temp%10
    b=a**3
    sum=sum+b
    temp=temp//10
if(n==sum):
    print('it is palindrome')
else:
    print('it is not palindrome')
