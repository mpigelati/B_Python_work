'''
ids = ["9pti", "2plv", "1crn"]
print ids

ids.append("1alm")
print ids

ids.append(10)
ids.append(ids[4] + 10)
print ids

#print "4-->",ids[4]
#print "5-->",ids[5]
#print "6-->",ids[6]

#ids[5] = ids[5] + 20
#$print ids

#del ids[0]
print " "
print ids

ids.sort()
print ids

ids.reverse()
print ids

ids.insert(2, "Mohan")
print "insert",ids
'''
list1 = ['physics', 'chemistry', '1997', '2000'];
list2 = [1, 2, 3, 2, 5, 2, 5, 2 ];
list3 = ["a", "b", "c", "d"]

#print "list1[0]: ",   list1[0]
#print "list2[1:5]: ", list2[1:5]

#print "l1",list1

#print "l1[2]",list1[2]

list1[2] = 2001;

#print list1[2]

#print "l1[2]_1",list1[2]

#print list1

del list1[2];
#print "del:- ",list1

list1.append(10)

#print list1

#print "l2:- " ,list2
#print "l1.count :- ",list2.count(2)
#print "l2_print:-",len(list2)

print "list1: ",   list1
print "list2: ",   list2
list1.extend(list2) #this adds all list2 elements to list1
print "list1: ",   list1
print "list2: ",   list2

print list1.index('chemistry')
print list1.index('physics')


print "list2: ",   list2
list2.pop()
list2.pop()
list2.pop()
list2.append(9)
print "list2: ",   list2
list2.pop(2)
list2.pop(0)
list2.pop(-1)
#list2.pop(10)
print "list2: ",   list2

list2.sort()
print "list2: ",   list2

list1 = ['physics', 'the subject is english is', 'chemistry', '1997', '2000'];

new_sub = "maths"
if (new_sub in list1):
    print "Found"
else:
    print "Appending"
    list1.append(new_sub)

new_sub = "english"
if (new_sub not in list1):
    print "Appending"
    list1.append(new_sub)

print list1

new_sub = "English"
if (new_sub not in list1):
    print "Appending"
    list1.append(new_sub)

print list1
