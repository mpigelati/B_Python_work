class student :


    def __init__(self,first,last,marks,sex):
        self.first=first
        self.last=last
        self.marks=marks
        self.sex=sex
        self.email=first+"0"+last+"@gmail.com"

std_1=student("Mohan","pigelati",30,"M")
std_2=student("Thanuja","pigelati",60,"F")
print(std_1.first)
print(std_2.first)

