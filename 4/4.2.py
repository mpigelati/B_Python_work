#!/usr/bin/python 

print "hellow world","\n"

  #print"my_list[i]",i,"my_list[j]",j
a=[3,5,3,10,15,20,3,5,10,20,3,25]

print "Before",a

i=j=k=0

n=11

'''while(i < n):
 print my_list[i]
 i+=1'''

i = 0

while(i < n ):
    print "\n\n\n"
    print"value",a[i]
    j=i+1
    while(j < n):
        print"while_loop2_i",i,"j",j
        print"while_loop2_my_list[i]",a[i],"my_list[j]",a[j]
        if(a[i]==a[j]):
            k=j;
            print"If_loop1_my_list[k]",a[k],"k:- ",k,'\n\n'
            print"while_loop3_my_list[k]",a[k],"my_list[j]",a[k+1]
            while(k < n ):
                print "k:- ",k
                print "k+1:- ",k+1
                print"before_while_loop3_my_list[k]",a[k],"my_list[j]",a[k+1]
                a[k]=a[k+1]
                #print"After_while_loop3_my_list[k]",a[k],"my_list[j]",a[k+1]
                k=k+1
                #n=n-1
                #print "n:->",n,"\n"
        j=j+1    
    print "After",a,"\n"
        
    print "\n\n\n"
    #n=n-1
    #print "n:->",n,"\n"
    i=i+1
 
print "After",a


