#StartedAt": "2017-07-11T15:07:59.869672233Z",

import datetime

def String_to_Date(Date_Time):
    print "Date and Time", Date_Time
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

    

