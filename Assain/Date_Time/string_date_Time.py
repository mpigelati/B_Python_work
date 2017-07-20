import datetime
def Convert_String_date_Time(String):
	print "This Function is to convert String `to date and time format:- ",String
	#print "date",String_To_Date
 	#2017-07-11T15:07:59.869672233Z
	YY,TT = String.split("T")
	Y,M,D = YY.split("-")
	HH,MM,SS =TT.split(".")[0].split(":")
        Date_Time = datetime.datetime(int(Y), int(M), int(D),int (HH),int (MM),int (SS))
	#print "Date",Date_Time        
	return Date_Time

