# auto_telnet.py - remote control via telnet
import os, sys, string, telnetlib
from getpass import getpass
def action(user, cmd_list):
        t = telnet
        t.write("\n")
        login_prompt = "login: "
        response = t.read_until(login_prompt, 5)
        if string.count(response, login_prompt):
            print response
        else:
            return 0
        t.write("%s\n" % user)
        response = t.read_until(password_prompt, 3)
        '''
        if string.count(response, password_prompt):
            print response
        else:
            return 0
        '''
        #t.write("%s\n" % self.passwd[user])
        t.write("%s\n" % "jnjnuh")
        response = t.read_until(self.command_prompt, 5)
        if not string.count(response, self.command_prompt):
            return 0
        for cmd in cmd_list:
            t.write("%s\n" % cmd)
            response = t.read_until(self.command_prompt, self.timeout)
            if not string.count(response, self.command_prompt):
                return 0
            print response
        return 1


telnet = telnetlib.Telnet()
telnet.open(host)
ok = action(user, cmd_list)
if not ok:
   print "Unable to process:", user
   telnet.close()

host = "127.0.0.1"
logname = "bhagavan"
passwd = "jnjnuh"
autoTelnet = AutoTelnet(logname, cmd_list, host=host)
