import thread
import os
import time
from multiprocessing import Process, Lock

my_global_variable = 0
tcount = 0

def printer(th_name, delay, lock):
    global my_global_variable 
    global tcount
    tcount += 1
    print '%d.%8s Before Modifying global data :%d' % (os.getpid(), th_name, my_global_variable)
    print '%d.%8s Locking critical section' % (os.getpid(), th_name)
    lock.acquire()
    print '%d.%8s Locking Success' % (os.getpid(), th_name)
    try:
        for i in range(1,4):
            print '%d.%8s **** In critical section...%d sec, global_data :%d' % (os.getpid(), th_name,  i, my_global_variable)
            time.sleep(delay)
            my_global_variable += 1
        print '%d.%8s Out of critical section...' % (os.getpid(), th_name)
    finally:
        print '%d.%8s Before Unlock, global data :%d' % (os.getpid(), th_name, my_global_variable)
        lock.release()
        print '%d.%8s After  Unlock, global data :%d' % (os.getpid(), th_name, my_global_variable)
        tcount -= 1
 
lock = Lock()
thread_names = ['ganga', 'kaveri', 'penna']
i = 1
new_threads_list = []

for tname in thread_names:
    #p = Process(target=printer, args=(th_name, lock))
    #p.start()
	try:
		nthread = thread.start_new_thread(printer, (tname, i, lock) )
		new_threads_list.append(nthread) 
		i += 1
	except:
		print "Error: unable to start thread"

c = raw_input("Type something to quit.")

print "Main process exiting"
