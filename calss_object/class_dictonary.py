class student:

    def __init__(self,first,last,marks,sex):

        self.fist=first
        self.last=last
        self.sex=sex
        self.matks=marks
        self.email= first+"."+last+"@gmail.com"

stu_1=student("Mohan","pigelati",30,"M")
stu_2=student("Thanuja","pigelati",30,"F")

print(stu_1)
print(stu_1.fist)
print(stu_2.fist)
print(stu_1.email)
print(stu_2.email)
print(stu_1.__dict__)
print(stu_2.__dict__)