'''The ratio of successful events A = 4 to total number of possible combinations of sample space S = 16 is the probability of 3 heads in 4 coin tosses. Users may refer the below detailed solved example with step by step calculation to learn how to find what is the probability of getting exactly 3 heads, if a coin is tossed four times or 4 coins tossed together.


Solution :
Step by step workout
step 1 Find the total possible combinations of sample space S
S = {HHHH, HHHT, HHTH, HHTT, HTHH, HTHT, HTTH, HTTT, THHH, THHT, THTH, THTT, TTHH, TTHT, TTTH, TTTT}

S = 16

step 2 Find the expected or successful events A
A = {HHHT, HHTH, HTHH, THHH}

A = 4

step 3 Find the probability
P(A) =Successful Events
Total Events of Sample Space

=4
16


= 0.25
P(A) = 0.25

0.25 is the probability of getting exactly 3 Heads in 4 tosses.'''



from itertools import product 
a=int(input('enter the number of possibilty of toss: '))
b=int(input('enter the number of head: '))
    
c=(list(product([a,b], repeat = a)))
print(c) #c is list that contain all the possible cartesian product 
d=a/len(c) # dividing it with number of possibilty
print(d)