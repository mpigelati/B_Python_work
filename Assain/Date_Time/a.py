import datetime
import sys

sys.path.append('/home/mohansai/python/B_Python_work/My_modile')
import  py35_string_date_Time

StartedAt= "2017-07-11T15:07:59.869672233Z"


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

Date_Time = py35_string_date_Time.Convert_String_date_Time(StartedAt)
print ("Date",Date_Time)        


