print("hellow world")
from telnetlib import Telnet

HOST= "localhost"
user ="manju"
password ="jnjnuhuh"

tn = Telnet(HOST)

tn.read_until("login: ")
tn.write(user +" \n")

if password :
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("ls\n")

