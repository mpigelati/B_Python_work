import time
import datetime
#import String_to_convert_Date_Time

#import String_to_convert_Date_Time
import Str_Date_Time
json_list = [
    {
        "Id": "dd3756c5eafcc219b531255a3e47c8054a610c24db57b25260d806848d05d9f4",
        "Created": "2017-07-11T15:07:58.990959648Z",
        "Path": "/bin/bash",
        "Args": [],
        "State": {
            "Status": "exited",
            "Running": "false",
            "Paused": "false",
            "Restarting": "false",
            "OOMKilled": "false",
            "Dead": "false",
            "Pid": 0,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2017-07-11T15:07:59.869672233Z",
            "FinishedAt": "2017-07-11T15:08:00.169576836Z"
        },
        "Image": "sha256:43e2c8843c069237612a00837ec38f988c109a92b3a2e145c31404eb2ae54424",
        "ResolvConfPath": "/var/lib/docker/containers/dd3756c5eafcc219b531255a3e47c8054a610c24db57b25260d806848d05d9f4/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/dd3756c5eafcc219b531255a3e47c8054a610c24db57b25260d806848d05d9f4/hostname",
        "HostsPath": "/var/lib/docker/containers/dd3756c5eafcc219b531255a3e47c8054a610c24db57b25260d806848d05d9f4/hosts",
        "LogPath": "/var/lib/docker/containers/dd3756c5eafcc219b531255a3e47c8054a610c24db57b25260d806848d05d9f4/dd3756c5eafcc219b531255a3e47c8054a610c24db57b25260d806848d05d9f4-json.log",
        "Name": "/ecstatic_stonebraker",
        "RestartCount": 0,
        "Driver": "aufs",
        "MountLabel": "",
        "ProcessLabel": "",
        "AppArmorProfile": "",
        "ExecIDs": "null",
        "HostConfig": {
            "Binds": "null",
            "ContainerIDFile": "",
            "LogConfig": {
                "Type": "json-file",
                "Config": {}
            },
            "NetworkMode": "default",
            "PortBindings": {},
            "RestartPolicy": {
                "Name": "no",
                "MaximumRetryCount": 0
            },
            "AutoRemove": "false",
            "VolumeDriver": "",
            "VolumesFrom": "null",
            "CapAdd": "null",
            "CapDrop": "null",
            "Dns": [],
            "DnsOptions": [],
            "DnsSearch": [],
            "ExtraHosts": "null",
            "GroupAdd": "null",
            "IpcMode": "",
            "Cgroup": "",
            "Links": "null",
            "OomScoreAdj": 0,
            "PidMode": "",
            "Privileged": "false",
            "PublishAllPorts": "false",
            "ReadonlyRootfs": "false",
            "SecurityOpt": "null",
            "UTSMode": "",
            "UsernsMode": "",
            "ShmSize": 67108864,
            "Runtime": "runc",
            "ConsoleSize": [
                0,
                0
            ],
            "Isolation": "",
            "CpuShares": 0,
            "Memory": 0,
            "CgroupParent": "",
            "BlkioWeight": 0,
            "BlkioWeightDevice": "null",
            "BlkioDeviceReadBps": "null",
            "BlkioDeviceWriteBps": "null",
            "BlkioDeviceReadIOps": "null",
            "BlkioDeviceWriteIOps": "null",
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "Devices": [],
            "DiskQuota": 0,
            "KernelMemory": 0,
            "MemoryReservation": 0,
            "MemorySwap": 0,
            "MemorySwappiness": -1,
            "OomKillDisable": "false",
            "PidsLimit": 0,
            "Ulimits": "null",
            "CpuCount": 0,
            "CpuPercent": 0,
            "IOMaximumIOps": 0,
            "IOMaximumBandwidth": 0
        },
        "GraphDriver": {
            "Name": "aufs",
            "Data": "null"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "dd3756c5eafc",
            "Domainname": "",
            "User": "",
            "AttachStdin": "false",
            "AttachStdout": "true",
            "AttachStderr": "true",
            "Tty": "false",
            "OpenStdin": "false",
            "StdinOnce": "false",
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
            ],
            "Cmd": [
                "/bin/bash"
            ],
            "Image": "auranetworks/bhagavannewtcpecho",
            "Volumes": "null",
            "WorkingDir": "",
            "Entrypoint": "null",
            "OnBuild": "null",
            "Labels": {}
        },
        "NetworkSettings": {
            "Bridge": "",
            "SandboxID": "09276b6a00c0e5cba08b55dc39b1c289fb60c7f0ccc403db819f4aa9bfe53801",
            "HairpinMode": "false",
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": "null",
            "SandboxKey": "/var/run/docker/netns/09276b6a00c0",
            "SecondaryIPAddresses": "null",
            "SecondaryIPv6Addresses": "null",
            "EndpointID": "",
            "Gateway": "",
            "GlobalIPv6Address": "",
            "GlobalIPv6PrefixLen": 0,
            "IPAddress": "",
            "IPPrefixLen": 0,
            "IPv6Gateway": "",
            "MacAddress": "",
            "Networks": {
                "bridge": {
                    "IPAMConfig": "null",
                    "Links": "null",
                    "Aliases": "null",
                    "NetworkID": "a46e96f8974dc153addefcf5cb341f81994f47de933c5fcc52695d51f7afaf44",
                    "EndpointID": "",
                    "Gateway": "",
                    "IPAddress": "",
                    "IPPrefixLen": 0,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "MacAddress": ""
                }
            }
        }
    }
]

#CONTAINER ID        IMAGE                             COMMAND             CREATED             STATUS                      PORTS      NAMES
#dd3756c5eafc        auranetworks/bhagavannewtcpecho   "/bin/bash"         11 minutes ago      Exited (0) 11 minutes ago              ecstatic_stonebraker

#print json_list
#print json_list[0]
#print type(json_list[0])







Start_Time_log = json_list[0]["State"]["StartedAt"]
End_Time_log = json_list[0]["State"]["FinishedAt"]

#print date_Time_log

'''
def String_to_Date(Date_Time):
    print Date_Time
    #2017-07-11T15:07:59.869672233Z
    
    Date,Hour = Date_Time.split("T")
    Hours= Hour.rstrip("Z")
   
    (HM,ML) = Hours.split(".")
                #(or) you can use any oh the way to split
    #HH,MI,SS  =Hours.split(".")[0].split(":")

    HR,MI,SS = HM.split(":")
    YY,MM,DD = Date.split("-")
    print HR,MI,SS
    print YY,MM,DD
    Date_Time = datetime.datetime(int(YY),int(MM),int(DD),int(HR),int(MI),int(SS))
    print "Date_Time",Date_Time
    return Date_Time
'''
#String_to_Date(date_Time_log)
Start_Time =Str_Date_Time.String_to_Date(Start_Time_log)
#print "Start:- ",Start_Time
End_Time = Str_Date_Time.String_to_Date(End_Time_log)
#print "End:- ",End_Time

Total= Start_Time- End_Time

print "Total %d",Total



print "CONTAINER ID        IMAGE                             COMMAND         CREATED             STATUS                      PORTS      NAMES"

#print "%-19s %-33s %-20s" %  (json_list[0]["Id"][0:12], json_list[0]["Config"]["Image"], json_list[0]["State"]["StartedAt"])

print "%-19s %-33s %-14s %-20s %-28s %-10s %-5s" %  (json_list[0]["Id"][0:12], json_list[0]["Config"]["Image"],json_list[0]["Config"]["Cmd"], Total, Total,json_list[0]["NetworkSettings"]["Ports"],json_list[0]["Name"])

print "\n\n\n"

'''print "CONTAINER ID        IMAGE                             COMMAND         CREATED             STATUS                      PORTS      NAMES"

print "%-19s %-33s %-20s" %  (json_list[0]["Id"][0:12], json_list[0]["Config"]["Image"], json_list[0]["State"]["StartedAt"])

print "%-19s %-33s %-16s %-33s %-50s %-19s %-10s" %  (json_list[0]["Id"][0:12], json_list[0]["Config"]["Image"],json_list[0]["Config"]["Cmd"], json_list[0]["State"]["StartedAt"], json_list[0]["State"]["FinishedAt"],
                                                      json_list[0]["NetworkSettings"]["Ports"],json_list[0]["Name"])'''



'''

datetime.datetime.now()

datetime_now=datetime.datetime.now()
datetime_today=datetime.datetime.today()


compare= "2017-07-12 06:11:50.073199"

#diff =(int)compare - datetime_today

print "compare:- ",diff
if(compare == datetime_today):
    print "both are same"
else:
     print"both are not same"




#datetime.datetime.now()

print datetime_now
print datetime_today

#print json_list[0]["State"]["StartedAt"]
#print json_list[0]["State"]["StartedAt"]
#print json_list[0]["Id"]
#print json_list[0]["Id"][0:12]
#print json_list[0]["Config"]
#print json_list[0]["Config"]["Cmd"]
#print json_list[0]["Name"]
#
#'''
