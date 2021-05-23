a=int(input('enter the number: '))
b=[]
while(a!=0):
    if(a%2==0):
        b.append(0)
    else:
        b.append(1)
    a=a/2
print(b)            
    