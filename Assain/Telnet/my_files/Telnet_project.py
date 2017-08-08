import telnetlib
import json
import unicodedata
#import thread
def Fun_Telnet(localhost,user,password):
    #localhost= localhost.encode('ascii', 'ignore')
    #print("type",type(localhost))

    HOST = localhost.encode('ascii', 'ignore')
    user = user.encode('ascii', 'ignore')
    password = password.encode('ascii', 'ignore')

    print(user)
    tn = telnetlib.Telnet(HOST)

    tn.read_until("login: ")
    tn.write(user + "\n")

    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")

    tn.write("ls -la\n")
    tn.write("exit\n")

    print (tn.read_all())



json_file = "data.json"
json_data = open(json_file)
data = json.load(json_data)

for i in range(0,len(data)):
    Fun_Telnet(data[i]["Host"],data[i]["user"],data[i]["password"])
