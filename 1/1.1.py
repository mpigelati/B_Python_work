#!/usr/bin/perl

n=642
Sum=0
while (n > 0):
 temp = n%10
 #print("temp:- ",temp)
 Sum=Sum+temp
 #print("Sum:- ",Sum)
 n=n//10
 print("==================")

print("Sum:- ",Sum)
