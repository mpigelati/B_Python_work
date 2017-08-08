import re
line ="cats are smarter then dogs"

matchobj = re.match(r'dogs',line,re.M|re.I)

if matchobj:

    print("Found")
else:
    print("Match not found")


searchobj=re.search(r'dog',line,re.M|re.I)

if searchobj:
    print("Match found")

else:
    print("Match not found")
