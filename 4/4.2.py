#!/usr/bin/python 

print "hellow world","\n"

  #print"my_list[i]",i,"my_list[j]",j
a=[3,5,3,10,15,20,3,5,10,20,3,25]

print "Before",a

i=j=k=0
count=0
n=11

'''while(i < n):
 print my_list[i]
 i+=1'''

i = 0

while(i < n ):
    j = i + 1
    while(j < n):
        if(a[i]==a[j]):
           k=j;
           while(k < n ):
               print"before_while_loop3_my_list[k]",a[k],"my_list[j]",a[k+1]
               a[k]=a[k+1]
               k=k+1
           n=n-1
           j=j-1 
        j=j+1    
    i=i+1
 
print "After",a


