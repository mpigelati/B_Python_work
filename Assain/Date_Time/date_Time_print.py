import datetime
import sys

sys.path.append('/home/mohansai/python/B_Python_work/My_modile')
import  py35_string_date_Time

StartedAt   = "2017-07-11T15:07:59.869672233Z"
FinishedAt  = "2017-07-15T17:08:00.169576836Z"


'''
def Convert_String_date_Time(String):
 #print ("This Function is to convert String `to date and time format", String)
 #print "date",String_To_Date
 #2017-07-11T15:07:59.869672233Z
 YY,TT = String.split("T")
 Y,M,D = YY.split("-")
 HH,MM,SS =TT.split(".")[0].split(":")
 Date_Time = datetime.datetime(int(Y), int(M), int(D),int (HH),int (MM),int (SS))
 #print "Date",Date_Time        
 return Date_Time
'''


def String_to_date(String):
 YDate = "07/27/2012"
 YtDate = datetime.datetime.strptime(YDate,"%m/%d/%Y")
 print ("1",YtDate)
 sDate = "2012/07/27"
 dtDate = datetime.datetime.strptime(sDate,"%Y/%m/%d")
 print ("2",dtDate)


String_to_date(StartedAt)

S_Date_Time = py35_string_date_Time.Convert_String_date_Time(StartedAt)
F_Date_Time = py35_string_date_Time.Convert_String_date_Time(FinishedAt)


Delta = S_Date_Time - F_Date_Time 

#Date_Time = py35_string_date_Time.Convert_String_date_Time(StartedAt)

print ("S_Date_Time",S_Date_Time)        
print ("F_Date_Time",F_Date_Time)        
print ("Delte",Delta)        



