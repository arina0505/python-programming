n=input('enter the str')
d=0
s=0
for i in n:
    if(i.isdigit()):
       d=d+1 
    else:
        s=s+1 
print(d,s)
if(d>0 and s>0):
    print('yes')
else:
    print('no')
