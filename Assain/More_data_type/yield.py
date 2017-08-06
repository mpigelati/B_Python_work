print ("this is yeald")
def fun():
    print("this is function")
    for i in range(0,3):
        print("i",i)
        print("iteration")
        yield i*i

M_generator=fun()
#print("generator",generator)
for i in M_generator:
    print("i:-%d"%i)


#for j in M_generator:
 #   print("j:-%d" % j)
