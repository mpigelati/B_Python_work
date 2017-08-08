import re

#===========================Match====================
line= "Cats are smarter than dogs"

matchobj= re.match(r'(.*) are(.?) .*',line,re.M|re.I)

if matchobj:
    print("matchobj.group:",matchobj.group())
    print("matchobj.group1:",matchobj.group(1))
    print("matchobj.group2:",matchobj.group(2))
else:
    print("no match")

line1 = "Cat are smarter than dogs"

#==========================search======================

searchobj = re.search( r'(.*) are (.*?) .*',line1,re.M|re.I)
#searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)

if searchobj:
    print("searchobj.group:", searchobj.group())
    print("searchobj.group1:",searchobj.group(1))
    print("searchobj.group2:",searchobj.group(2))
    #print("searchobj.group2:",searchobj.group(3))
else:
    print("no match")


