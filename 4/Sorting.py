#!/usr/bin/python 

#print "hellow world"


def swap(i,j):
 #print "Swap finction"
 print ("swap",i, j)
 i=i+j
 j=i-j
 i=i-j
 print ("i",i, j)


n = 7
i = 0

a = [5,3,4,1,2,7,6]
print "before_sort_List", a

i = j = k = 0

while(i < n ):
 #print "===first_loop==="
 #print "1:- list",a
 j=i+1
 while(j < n):
  #print ("===Second_loop===\n")
  #print ("before_swap",a[i], a[j])
  
  if(a[i] > a[j]):
   
    a[i]=a[i]+a[j]
    a[j]=a[i]-a[j]
    a[i]=a[i]-a[j]
  
  #swap(a[i],a[j])
  #print ("after_swap",a[i], a[j])
  
  j+=1
  #print ("End_2==j=",j,"\n")
  #print "list",a,"\n"
  #print ("before_swap",a[i], a[j])
 
 i+=1
 #print ("===1===")
print "After_sort_List", a

