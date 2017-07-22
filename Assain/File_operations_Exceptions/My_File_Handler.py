#print ("hellow world")

import datetime

S_File_name =  ("/home/mohansai/PycharmProjects/MY_sample/B_Python_work/Assain/File_operations_Exceptions/D.txt")
D_File_name =  ("/home/mohansai/PycharmProjects/MY_sample/B_Python_work/Assain/File_operations_Exceptions/t.txt")


def File_open(File_Name,mode):
    try:
        fd =  open(File_Name,mode)
    except IOError:
        print ("Failed to open file", File_Name)
        exit(1)
    else:
        print("Successfully opend file")
        return fd

S_File_Fd = File_open(S_File_name,"r")
#D_File_Fd = File_open(D_File_name,"w")

print (S_File_Fd)

for line in S_File_Fd:
    print (line)

