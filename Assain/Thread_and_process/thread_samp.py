import _thread
import time


def Thread_Start(name,Duration):
	print(" you are in thread:-1 ");
	count=0
	while 1:
		time.sleep(Duration)
		print ( "name:- %s" % name,time.ctime(time.time()))
		if count == 5:
			exit(1)
		
		count+=1

try:
	_thread.start_new_thread(Thread_Start,("Mohan",2))
	_thread.start_new_thread(Thread_Start,("Thanuja", 2))
except:
	print ("failed to crate thread")
else:
	print ("Thread created successfully")

while 1:
	pass
#Theread_Start_1("name",2)
	


