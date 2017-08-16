import json
import subprocess

gitlog= "git log > git_log.txt"
subprocess.call(gitlog,shell=True)
#with open('data.json','r') as js:
 #   print(js)

my_json={}
my_json=[]

def Fun_json_print():
    with open("data.json","r") as pd:
        data = json.load(pd)
        print(data)
    #for line in data:
    #  print(line["commit"])

def Fun_json(my_list):
    #print("mylist",my_list)
    #print("my_list_len",len(my_list))
    my_json.append(
            {
                "commit":my_list[0].split[" "][1].rsplit("\n")
                "Auther":my_list[1],
                "Date" :my_list[2],
                "Text":my_list[3].lstrip(" ")
            })
    with open("data.json", 'w')as fd:
        #print(fd)
        json.dump(data,fd)



with open('git_log.txt','r') as fd:
    print(fd)
    data =fd.readlines()
    size=len(data)-1
    #print("size",size)
    t_list=[]

for i, line in enumerate(data):
    if("commit" in line and size != i):
        for j in range(i,i+5):
            if(data[j] != "\n"):
                t_list.append(data[j])
        Fun_json(t_list)
        #print(t_list)
        t_list.clear()

Fun_json_print()