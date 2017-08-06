#print("hellow world")
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
number = "415-555-4242"
number1 = "415-555-4242"
def Fun_phonenum(num):
    #print("num ",num)

    if(len(num) != 12):
        return False
    for i in range (0,3):
        if not num[i].isdecimal():
            return False
    if num[3] != '-':
         return  False
    for i in range(4,7):
        if not num[i].isdecimal():
            return False
    if num[7] != '-':
        return False
    for i in range(8, 12):
        if not num[i].isdecimal():
            return False

    return True

for i in range(len(message)):
     chunk = message[i:i+12]
     #print(i,chunk)
     if Fun_phonenum(chunk):
        print('Phone number found: ' + chunk)
        print('Done')
'''
#temp = Fun_phonenum(number)
#print(temp)

print('415-555-4242 is a phone number:')
print(Fun_phonenum('415-555-4242'))
print('Moshi moshi is a phone number:')
print(Fun_phonenum('Moshi moshi'))
'''