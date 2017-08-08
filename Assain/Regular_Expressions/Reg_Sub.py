import  re

phone = "2004-959-559" # this is phone number

match=re.sub(r'#.*$',"",phone)

print(match)

match1=re.sub(r'\D',"",phone)
print(match1)
'''
if match:

    print("pass")
else:
    print("fail")
'''

