import json

'''jsonData = '{"name": "mohan", "age": 31}'
data = json.loads(jsonData)
print(data)

jsonData1 = {"name":"sakethram","age":12}

data1=json.dumps(jsonData1)
print(data1)'''


#================= This  is sample json data format====================
'''data = {}

data['people']=[]

data['people'].append(
        {

        'commit':'mohan',
        'time'  : '12:25',
        'name'  :'mohan'
        }
    )
data['people'].append(
        {

        'commit':'saketh',
        'time'  : '12:25',
        'name'  :'saketh'
        }
    )

data['people'].append(
        {

        'commit':'lekshana',
        'time'  : '12:25',
        'name'  :'lekshana'
        }
    )

with open('data.txt','w')as fd:
    json.dump(data,fd)


with open("data.txt","r") as fp:
    data= json.load(fp)
    print(data)
    #print(len(data))

#data[0]["time"]

for i in data['people']:
    print(i['name'])
'''

data={}
data=[]
#data['data']
data.append(
        {

        'commit':'mohan',
        'time'  : '12:25',
        'name'  :'Mohan'
        }
    )
data.append(
        {

        'commit':'saketh',
        'time'  : '12:25',
        'name'  :'saketh'
        }
    )
data.append(
        {

        'commit':'lekshana',
        'time'  : '12:25',
        'name'  :'lekshana'
        }
    )
with open("data.json","w") as fd:
    json.dump(data,fd,indent=2)

with open("data.json","r") as fd:
    data = json.load(fd)
    #print(data)
for line in data:
    print(line["name"])