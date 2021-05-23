a=input('entre the number: ')
b=[]
c='23456789'
if (a not in c):
    for i in range(len(a)):
       b.append(int(a[i]))
sum=0 
print(b) 
b.reverse()
for i in range(len(b)):
      sum+=pow(2,i)*b[i]
      
print(sum)      