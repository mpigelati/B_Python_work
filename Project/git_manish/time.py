from datetime import datetime

#datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')

#print(datetime_object)

#temp_time= "Tue Aug 1 14:55:13 2017 +0530"
#temp1 =temp_time.split("+")[0]
#print(temp1)

temp_time1="Tue Aug 1 14:55:13 2017"

#datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')

#                        temp_time1="Tue Aug 1 14:55:13 2017"

datetime_object = datetime.strptime('Tue Aug 1 14:55:13 2017','%a %b %d %H:%M:%S %Y')
print(datetime_object)