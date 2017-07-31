import subprocess
import os
#import subprocess32 as sub


try :

    fd =open("samp.txt","w")
except:
        print("failed to open file")

else :
    print("file opened successfilly")

cmd =["ls", "-la"]
subprocess.call(cmd, stdout=fd)
#out.close()

#subprocess.call(["ls","-la >"],stdout=fd)

#subprocess.call(["ls","-la >"], stdout=fd)



#subprocess.call('du -hs $HOME', shell=True)
#subprocess.call(["ls","-la",">samp.txt"],shell=True)
#subprocess.call('ls -la >samp.txt', shell=True)
