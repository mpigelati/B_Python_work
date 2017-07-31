#print ("Email validation")

list_Eaddr = ["gmail.com", "gmail.co.in","yahoo.com","yahoo.co.in","qti.qualcomm.com","qualcomm.com"]

Email= "saimohansai@qti.qualcomm.com"

Name,Eaddr = Email.split('@')

#print ("Name:- %s " % Name)
#print ("Eaddr:-%s " % Eaddr)


for L_Eaddr in list_Eaddr:
    #if Eaddr == gmail.com
    #print("Eaddr:- %s" % L_Eaddr)
    if Eaddr == L_Eaddr:
        print("it is valied address")
