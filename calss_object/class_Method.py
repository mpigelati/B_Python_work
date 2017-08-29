class student :


    def __init__(self,fist,last,marks,sex):

        self.first=fist
        self.last=last
        self.sex=sex
        self.marks=marks

stu_1=student("Mohan","pigelati",32,"M")
stu_2=student("Thanuja","pigelati",55,"F")

print('{} {}'.format(stu_1.first,stu_1.last))
print('{} {}'.format(stu_2.first,stu_2.last))
print(stu_1.__class__)
print(stu_1.__dict__)


