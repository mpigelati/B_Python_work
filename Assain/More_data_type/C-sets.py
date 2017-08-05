my_set = {1, 2, 3, 8, 4}

#print (type(my_set))
#print(my_set)

# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
#print(my_set)

my_set = set([1,2,3,2])
print(my_set)

a = {}
print(type(a))

a = set()
print(type(a))

my_set = {1, 2, 3}
print("1",my_set)

my_set.add(5)
print("2",my_set)
my_set.add(0)
print("3",my_set)

my_set.update([2,3,4])
print("4",my_set)

my_set.update([4,5], {1,6,8}, (9,10))
print("5",my_set)

print ("")
my_set = {1, 3, 4, 5, 6}
print("6",my_set)

my_set.discard(3)
print("7",my_set)

my_set.remove(6)
print("8",my_set)

my_set.discard(2)
print("9",my_set)

#my_set.remove(2)
print("10",my_set)

print ("")
my_set = set("HelloWorld")
print("11",my_set)

print(my_set.pop())

my_set.pop()
print(my_set)

my_set.clear()
print(my_set)

print ("")
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print ("A ", A)
print ("B ", B)

print("|",(A | B))
print ("A",A.union(B))
print ("B",B.union(A))

print ((A & B))
print (A.intersection(B))
print (B.intersection(A))

print ("")
print("-",(A - B))
print (A.difference(B))

print((B - A))
print (B.difference(A))

print ("")
print("^",(A ^ B))
print (A.symmetric_difference(B))

print((B ^ A))
print (B.symmetric_difference(A))
print ("")
