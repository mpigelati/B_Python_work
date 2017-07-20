import datetime
#import sys

import Mohan_string_date_Time

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
    ]

A_StartedAt = json_list[0]["State"]["StartedAt"]
A_FinishedAt= json_list[0]["State"]["FinishedAt"]

Date_Time =Mohan_string_date_Time.Convert_String_date_Time(A_StartedAt)
print "Date",Date_Time        


