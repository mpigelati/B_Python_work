class student:

    #perc_rise = 1.05

    def __init__(self,first,last,sex,marks):
        self.first=first
        self.last=last
        self.sex=sex
        self.marks=marks

    def fullname(self):

        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):

        self.marks = int(self.marks* 1.05)

stu_1=student("Mohansai","pigelati","M",55)
stu_2=student("Thanuja","pigelati","F",30)

print(stu_1.first)
print(stu_2.first)

print(stu_1.fullname())
print(stu_1.marks)
print(stu_1.apply_raise())
print(stu_1.marks)
print(stu_2.fullname())
print(stu_2.marks)
print(stu_2.apply_raise())
print(stu_2.marks)
