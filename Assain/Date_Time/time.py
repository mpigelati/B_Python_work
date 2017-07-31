import time
import datetime


print(time.time())
print(time.ctime(time.time()))

print(datetime.datetime.now())
print(datetime.datetime.now().strftime("%y-%m-%d-%H-%M"))
      #datetime.datetime.now().strftime("%y-%m-%d-%H-%M"))
print ("Time in seconds since the epoch: %s" %time.time())

print ("Current date and time: " , datetime.datetime.now())

print ("Or like this: " ,datetime.datetime.now().strftime("%y-%m-%d-%H-%M"))