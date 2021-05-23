a=input('entre the number: ')
b=[]
if ('1' in a)and ('0' in a):
    for i in range(len(a)):
       b.append(int(a[i]))
sum=0 
print(b) 
b.reverse()
for i in range(len(b)):
      sum+=pow(2,i)*b[i]
      
print(sum)      