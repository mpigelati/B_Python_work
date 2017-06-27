#!/usr/bin/python


print "hellow world","\n"

n = 8

my_list=[10,20,3,20,10,30,4,50]
print "Before"
print my_list,"\n"

i=j=k=0

'''while (i < n):
 print my_list[i]
 i+=1'''


i=0

while(i < n ):
 #print"===Loop:-1==="
 #print"i",i
 j=i+1
 while(j < n ):
  #print"===Loop:-2==="
  #print my_list[i],"==",my_list[j]
  if(my_list[i] == my_list[j]):
   #print "TRUE"
   my_list[j]=0
  j=j+1
  #print"j",j
 i=i+1


print "Before"
print my_list,"\n"

