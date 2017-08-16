import time
from datetime import datetime

temp_time = "Sat Aug 12 17:02:10 2017 +0530"


def M_time_convert(Time):
    return datetime.strptime(Time, '%a %b %d %H:%M:%S %Y')


def M_Time_diff(M_time):

    M_temp = M_time_convert(temp_time.split("+")[0].rstrip(" "))
    print(M_temp)
    M_temp1 = M_time_convert(time.ctime(time.time()))
    print(M_temp1)
    diff = M_temp - M_temp1
    print("diff", diff)


diff = M_Time_diff(temp_time)