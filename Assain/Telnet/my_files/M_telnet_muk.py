from telnetlib import Telnet
from sys import argv

def Fun_to_open_file(filename,mode):
    try:
        fd= open(filename,mode)
    except:
        print("failed to open file")
    else:
        return fd

fd = Fun_to_open_file(argv[1],"r")
data = fd.readlines()
#print("data",data)
date=[]
for line in data:
    if ("userip" in line) | ("username" in line )|("password" in line):
        #print(line)
        value = "".join(line.split(":")[0])
        keys = "".join(line.split(":")[1])
        print("user:- %s:-, key:- %s" % (value, ))
        temp = value.strip("\t").strip(' /"')
        temp1 = keys.strip("\t").strip(' /"')
        print("user:- %s:-, key:- %s" % (temp,temp1))

Host="localhost"
user= "lekshana"
password = "jnjnuhuh"



'''
tn = Telnet(Host)
print("telnet",tn)

tn.read_until("login: ")
tn.write(user +"\n")

if password:
    tn.read_until("Password: ")
    tn.write(password +"\n")

tn.write("ls -la \n")

tn.write("exit\n")
print (tn.read_all())
'''




