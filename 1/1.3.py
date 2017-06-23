#!/usr/bin/python 

n=626
O_n = n
print("n:- ",n)
c=0 
while( n > 0):
  Temp = n % 10
  c=c*10+Temp 
  n=n//10
 
print("c:- ",c)

if(O_n == c):
 print("palindrome")
else:
 print("not palindrome")

