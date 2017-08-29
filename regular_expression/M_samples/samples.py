import re

#regex = r"([a-zA-Z]+) (\d+)"

'''regex = r"([a-zA-Z]+) (\d+)"

match  = re.search(regex,"Augest 24")
if(match):
    print("match index",match.start(),match.end())
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    #print(match.group(3))# error
else:
    print("not matching ")

#regex = r"[a-zA-Z]+ \d+"
#matches = re.findall(regex, "June 24, August 9, Dec-12")
#for match in matches:
#    print ("Full match: %s" % (match))'''


#regex1=r"([A-Za-z]+ \d+)"
#matches =re.findall(regex1,"sep 1 sep 3 sep 9")
#for match in matches:
#    print("match ",match)

#string = "Saimohansai879"# working
#reg=r"([A-Za-z]+)(\d+)"

string= "saimohansai879"
reg=r"([A-Za-z]+)(\d+)"
str_matches= re.match(reg,string)

if(str_matches):
    print("matching")
else:
    print("not matching")
