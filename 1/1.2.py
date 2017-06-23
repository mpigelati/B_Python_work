#!/usr/bin/perl

n=426
Mul=0
Sum=1

print("n:- ",n)

while (n > 0):
 temp = n%10
 #print("temp:- ",temp)
 Mul = Mul*10+temp
 #print("Mul:- ",Mul)
 n=n//10
 #print("n:- ",n)
 #print("==================")

print("mul:- ",Mul)
