n=int(input('enter the number'))
temp=n
rev=0
while(n>0):
    value=n%10
    rev=rev*10+value
    n=n//10
if(temp==rev):
    print('it is palindrome')
else:
    print('it is not palindrome')
