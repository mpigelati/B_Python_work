import subprocess
#import subprocess32 as sub
'''
with open("file1.txt","a") as f:
    f.flush()
    sub.Popen(["cat","temp.txt"],stdout=f)


try :

    fd =open("samp.txt","w")
except:
        print("failed to open file")

else :
    print("file opened successfilly")


subprocess.call(["ls","-la >" ," >"], stdout=fd)
subprocess.call(["ls","-la >"],stdout=fd)

subprocess.call(["ls","-la >"], stdout=fd)


input_files = ['file1', 'file2', 'file3']
my_cmd = ['cat'] + input_files
with open('myfile', "w") as outfile:
subprocess.call(my_cmd, stdout=outfile)'''

#subprocess.call('du -hs $HOME', shell=True)
#subprocess.call(["ls","-la",">samp.txt"],shell=True)
subprocess.call('ls -la >samp.txt', shell=True)
