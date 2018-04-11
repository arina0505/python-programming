a=[]
n=int(input('enter the number'))
for i in range(n):
  b=int(input('enter the numbers'))
  a.append(b)
  a.sort()
print(a)
x=n//2
print(a[x])
