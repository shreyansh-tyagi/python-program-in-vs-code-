from itertools import product
a,b=map(int,input('enter two numbers: ').split())
print("The cartesian product using repeat:") 
d=(list(product([a,b], repeat = a))) 
print(d)
c=(len(d))
print(c)
b=a/c
print(b)