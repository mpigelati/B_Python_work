
#!/usr/bin/python3


tuple1, tuple2 = (123, 'xyz'), (456, 'abc')


#print ("T1", tuple1)
#print ("T2", tuple2)

print " "
print cmp(tuple1, tuple2)
print cmp(tuple2, tuple1)

tuple3 = tuple2 + (786,);
print cmp(tuple2, tuple3)

print ("T2", tuple2)
print ("T3", tuple3)


tuple1 = (123, 'abcdef')
tuple2 = (123, 'abb')

print cmp(tuple1, tuple2)
print cmp(tuple2, tuple2)
print cmp(tuple2, tuple1)
#print tuple1, (123, 'ab'))
print cmp(tuple1, (123, 'ab'))

print ""
'''


print "1",cmp((123, 'abc'), (123, 'abc'))
print "2",cmp((123, 'abc'), (123, 'abz'))
print "3",cmp((123, 'abc'), (123, 'aba'))
print "4",cmp((123, 'abc'), (123, 'abaxyz'))
print "5",cmp((123, 'abc'), (123, 'abdxyz'))
print "6",cmp((123, 'abc'), ('123', 'abdxyz'))

print ""


tuple1 = (123, 'abcdef')
tuple2 = (123, 'abb')

#tuple3 = tuple2 + ('823')
tuple3 = tuple2 + tuple('823')
print tuple3
print cmp(tuple2, tuple3)

print ""
tuple1 = tuple('823')
print tuple1
print type(tuple1)

tuple1 = tuple("823")
print tuple1
print type(tuple1)


tuple1 = (123, '283')
print tuple1

print tuple1[0]
print type(tuple1[0])
print tuple1[0]+5
print int(tuple1[1])+5

tuple1 = (123, '283')
tuple2 = (123, 'abb')

print "First tuple length : ",  len(tuple1)
print "Second tuple length : ", len(tuple2)
exit(1)

tuple1 = ('1834', 98346 )
tuple2 = (123, 'abb')

print "tuple1 :", tuple1
print "tuple2 :", tuple2
#print dir(tuple1)
#print dir(tuple1.__doc__)
print "Max value element tuple1: ", max(tuple1)
print "Max value element tuple2: ", max(tuple2)

print "min value element : ", min(tuple1)
print "min value element : ", min(tuple2)


tuple1 = ('1834', 98346 )
tuple2 = (123, 'abb')

print ""
aList = (123, 'xyz', 'zara', 'abc');
aTuple = tuple(aList)
print "Tuple elements : ", aTuple


tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5, 6, 7 );
print "tup1[0]  : ", tup1[0]
print "tup2[1:5]: ", tup2[1:5]

print "tup1  :", tup1
print "tup2  :", tup2
exit(1)

tup1 = (12, 34.56);
tup2 = ('abc', 'xyz');

#print "tup1  :", tup1
#print "tup2  :", tup2

#tup1[0] = 100;
#tup1.append(4)

#del tup1;
print ""
print "tup1  :", tup1

tup3 = tup2 + tup1 + tup2 + (2, 3, 4, 5)
print "tup3  :", tup3


tup = ('physics', 'chemistry', 1997, 2000);
del tup;
print "tup :", tup

print "After deleting tup..."
print "tup :", tup

exit(1)

julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
(name, surname, b_year, movie, m_year, profession, b_place) = julia

print name, surname,b_year,movie
exit(1)

print ""
months = ('', 'January','February','March','April','May','June', 'July','August','September','October','November','  December')
print "months :", months

print ""
x = 8
print months[x]
print len(months)

#months.sort()
print "months :", months
exit(1)
'''
