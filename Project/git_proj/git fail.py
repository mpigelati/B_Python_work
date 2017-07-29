#print ("hellow world")
import subprocess
import os
#subprocess.call()
#subprocess.call(("ls","-la"))
#list_comm_1 = ("ls","-la")
#list_comm = ("git","status",">","samp.txt")
#subprocess.call(list_comm)

os.system("git status > status.txt")

#print(subprocess(["cat",""]))
def Fun_print_file(Fd):
    Zip=[]
    #print ("please print file content")
    String="modified"
    P_list = Fd.readlines()
    for line in P_list:
        #print (line)
        if(line !='\n'):
            if line[-3:-1]=='py' or line[-4:-1]=='txt':
                temp = "".join(line.strip().split(':')[0])
                #temp1,temp2 = line.strip().split(':')
                if (temp == String):
                    temp1 = "".join(line.strip().split(':')[1])
                    temp1=temp1.strip()
                    Zip.append(temp1)
                    print(temp)

def Fun_open_File(Filename,mode):
    try:
        fd= open(Filename,mode)
    except:
        print("unable to open file")
        exit(1)
    else:
        #print("file opened success fully")
        return fd

Fd = Fun_open_File("status.txt","r")

Fun_print_file(Fd)