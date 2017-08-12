import time
#import datetime
from datetime import datetime
print("this is sample python")

temp_time= "Tue Aug 1 14:55:13 2017 +0530"

tick=time.time()
#print(tick)
#temp  = time.ctime(time.time())
#print("temp",temp)
#print("temp",temp1)
#T_diff= temp- temp1
#print(time.ctime(time.time()))

def M_time_convert(Time):
    return datetime.strptime(Time, '%a %b %d %H:%M:%S %Y')
    #print("M_time", datetime_object)


def M_date_Time_convert(M_time):

    temp1 = temp_time.split("+")[0].rstrip(" ")
    #print(temp1)
    M_temp=M_time_convert(temp1)
    print(M_temp)
    #print(type(M_temp))
    # datetime_object = datetime.strptime('Tue Aug 1 14:55:13 2017', '%a %b %d %H:%M:%S %Y')
    M_temp1 = M_time_convert(time.ctime(time.time()))
    print(M_temp1)
    #M_temp1 = M_time_convert(time.ctime(time.time()))



diff = M_date_Time_convert(temp_time)