
def myfun():
    #....
    yield 15

    #....
    yield "temp"

    #....
    yield 'a'

def createGenerator():
    mylist = range(5)
    #print ("mylist type :", type(mylist))
    #print ("my_list",mylist)
    for i in mylist:
        #print("i:-",i)
        yield i*i


#(a, b, c) = myfun()
#print ("a :%d, b :%s, c :%c" % (a, b, c))

#for item in myfun():
 #   print (item)

mygenerator = createGenerator()
#print ("genarator",type(mygenerator))
print ("data",mygenerator)

for i in mygenerator:
     print(i)

'''
#Returning multiple values from function

def M_fun():
    a=10
    b=20
    c=30
    return a,b,c

(a,b,c)=M_fun()

print("a:- %d b:- %d c:-%d" %(a,b,c))
'''