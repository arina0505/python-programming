a=int(input('enter the number'))
b=int (input('enter the number'))
for i in range(a,b):
   if (i>1):
       for n in range(2,i):
           if (i%n== 0):
               break
       else:
           print(i)
