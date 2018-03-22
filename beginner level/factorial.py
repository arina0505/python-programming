n=int(input('enter the number'))
l=len(str(n))
product=1
for i in range(1,n+1):    
  a=i%(10**l)    
  product=product*a
print(product)
